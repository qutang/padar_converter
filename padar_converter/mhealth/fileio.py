import pandas as pd


def load_sensor(filepath):
    if filepath is None:
        return None
    return pd.read_csv(filepath, parse_dates=[0], infer_datetime_format=True)


def load_annotation(filepath):
    if filepath is None:
        return None
    return pd.read_csv(filepath, parse_dates=[0, 1, 2], infer_datetime_format=True)
