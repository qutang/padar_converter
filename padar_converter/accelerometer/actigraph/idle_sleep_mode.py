import pandas as pd
import numpy as np


class IdleSleepModeConverter:
    def __init__(self, init_fill=None, init_is_ism=None):
        if init_fill is not None:
            self._current_fill = init_fill
        else:
            self._current_fill = pd.DataFrame()
        if init_is_ism is not None:
            self._before_is_ism = init_is_ism
        else:
            self._before_is_ism = pd.DataFrame()
        self._converted = pd.DataFrame()

    def get_ism(self):
        return self._ism_df

    def get_closest_fill(self, st):
        df = self._df.set_index(self._df.columns[0])
        fills = self._is_fill[self._is_fill.index <= st]
        if not fills.empty:
            fill_et = fills.index[-1] + pd.Timedelta(1, unit='s')
            fill_st = fill_et - pd.Timedelta(10, unit='s')
            self._current_fill = df[(df.index >= fill_st)
                                    & (df.index < fill_et)]
        return self._current_fill

    def detect_ism(self):
        self._current_is_ism = self._df.groupby(pd.TimeGrouper(
            freq='1s', key=self._df.columns[0])).apply(self._detect_ism)

    def _detect_ism(self, df):
        df = df.set_index(df.columns[0])
        unique_counts = df.apply(lambda col: len(col.unique()), axis=0)
        return np.all(unique_counts == 1)

    def detect_fill(self):
        if self._before_is_ism is not None:
            is_ism = pd.concat(
                [self._before_is_ism.iloc[-9:, ], self._current_is_ism], axis=0)
        else:
            is_ism = self._current_is_ism
        self._is_fill = is_ism.rolling(10).apply(
            lambda df: np.all(df == False)).dropna()
        self._is_fill = self._is_fill[self._is_fill.values == 1]

    def reverse_ism(self):
        current_is_ism = self._current_is_ism.reset_index(drop=False)
        self._filled_ism_counts = current_is_ism.groupby(
            pd.TimeGrouper(freq='10s', key=current_is_ism.columns[0])).apply(self._reverse_ism)

    def _reverse_ism(self, is_ism):
        is_ism = is_ism.set_index(is_ism.columns[0])
        st = is_ism.index[0]
        et = is_ism.index[-1] + pd.Timedelta(1, unit='s')

        if np.all(is_ism == True):  # the entire 10s is in ISM mode
            to_fill = self.get_closest_fill(st)
            if to_fill.empty:
                return 0
            indices = (self._converted.index >= st) & (
                self._converted.index < et)
            if np.any(indices):
                self._converted[indices] = to_fill.values
                return is_ism.shape[0]
            else:
                return 0
        # there are multiple seconds in ISM mode but not the entire 10s
        elif np.any(is_ism == True):
            is_ism = is_ism[is_ism.values]
            st = is_ism.index[0]
            et = is_ism.index[-1] + pd.Timedelta(1, unit='s')
            to_fill = self.get_closest_fill(st)
            if to_fill.empty:
                return 0
            indices = (self._converted.index >= st) & (
                self._converted.index < et)
            # use the first N seconds' non-ISM mode data to fill
            if np.any(indices):
                self._converted[indices] = to_fill.iloc[:np.sum(indices), :].values
                return is_ism.shape[0]
            else:
                return 0
        else:
            return 0

    def run(self, df, update=True):
        self._df = df
        self._converted = df.copy(deep=True)
        self._converted = self._converted.set_index(self._converted.columns[0])

        self.detect_ism()

        self.detect_fill()

        self.reverse_ism()

        if update:
            self._before_is_ism = self._current_is_ism

        return self

    def get_converted(self):
        return self._converted.reset_index(drop=False)

    def get_filled_ism_counts(self):
        return self._filled_ism_counts


if __name__ == '__main__':
    import sys
    import os
    import glob
    from padar_converter.mhealth.fileio import load_sensor
    converter = IdleSleepModeConverter()
    filepaths = glob.glob(os.path.join(sys.argv[1], '*.csv.gz'))
    for filepath in filepaths:
        print('Convert ' + filepath)
        df = load_sensor(filepath)
        df = df.reset_index(drop=False)
        converted_df = converter.run(df, update=True).get_converted()
        output_filepath = os.path.join(sys.argv[2], os.path.basename(
            filepath).replace('.gz', '').replace('.csv', '-reversed_ism.csv'))
        converted_df.to_csv(output_filepath, index=False)
