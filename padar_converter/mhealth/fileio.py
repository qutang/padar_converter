import pandas as pd


def load_sensor(filepath):
    if filepath is None:
        return None
    result = pd.read_csv(filepath, parse_dates=[0], infer_datetime_format=True)
    result = result.rename(columns = {result.columns[0]: 'HEADER_TIME_STAMP'})
    result.set_index(result.columns[0], inplace=True)
    return result


def load_annotation(filepath):
    if filepath is None:
        return None
    result = pd.read_csv(filepath, parse_dates=[0, 1, 2],
                         infer_datetime_format=True)
    result.set_index(result.columns[[0, 1, 2]], inplace=True)
    return result
