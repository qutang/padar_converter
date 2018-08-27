"""

Conversion function for Actigraph devices

"""
import pandas as pd
import os


def convert_actigraph_csv(data):
    if isinstance(data, str) and os.path.isfile(data):
        data = pd.read_csv(data,
                           parse_dates=[0], skiprows=10,
                           infer_datetime_format=True, engine='c')
        data.columns = ['HEADER_TIME_STAMP', 'X', 'Y', 'Z']
    return data


if __name__ == '__main__':
    import sys
    o = convert_actigraph_csv(sys.argv[1])
    print(o.head())
