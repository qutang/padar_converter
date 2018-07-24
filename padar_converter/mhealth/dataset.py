import re
import os
from datetime import datetime

CAMELCASE_PATTERN = r'(?:[A-Z][A-Za-z0-9]+)+'
VERSIONCODE_PATTERN = r'(?:NA|[0-9x]+)'
SID_PATTERN = r'[A-Z0-9]+'
ANNOTATOR_PATTERN = r'[A-Za-z0-9]+'
FILE_TIMESTAMP_PATTERN = r'[0-9]{4}(?:\-[0-9]{2}){5}-[0-9]{3}-(?:P|M)[0-9]{4}'
FILE_EXTENSION_PATTERN = r'''
(?:sensor|event|log|annotation|feature|class|prediction|model|classmap)\.csv
'''
MHEALTH_FLAT_FILEPATH_PATTERN = r'(\w+)[\/\\]{1}(?:(?:MasterSynced[\/\\]{1})|(?:Derived[\/\\]{1}(?:\w+[\/\\]{1})*))[0-9A-Za-z\-\.]+\.csv'
MHEALTH_FILEPATH_PATTERN = r'(\w+)[\/\\]{1}(?:(?:MasterSynced[\/\\]{1})|(?:Derived[\/\\]{1}(?:\w+[\/\\]{1})*))\d{4}[\/\\]{1}\d{2}[\/\\]{1}\d{2}[\/\\]{1}\d{2}'


def is_mhealth_filepath(filepath):
    filepath = os.path.abspath(filepath)
    matched = re.search(
        MHEALTH_FILEPATH_PATTERN,
        filepath)
    return matched is not None


def is_mhealth_flat_filepath(filepath):
    matched = re.search(
        MHEALTH_FLAT_FILEPATH_PATTERN,
        os.path.abspath(filepath)
    )
    return matched is not None


def is_mhealth_filename(filepath):
    filename = os.path.basename(filepath)

    sensor_filename_pattern = '^' + CAMELCASE_PATTERN + '\-' + CAMELCASE_PATTERN + \
        '\-' + VERSIONCODE_PATTERN + '\.' + \
        SID_PATTERN + '\-' + CAMELCASE_PATTERN + '\.' + \
        FILE_TIMESTAMP_PATTERN + '\.sensor\.csv$'

    annotation_filename_pattern = '^' + CAMELCASE_PATTERN + '\.' + \
        ANNOTATOR_PATTERN + '\-' + CAMELCASE_PATTERN + '\.' + \
        FILE_TIMESTAMP_PATTERN + '\.annotation\.csv$'

    sensor_matched = re.search(
        sensor_filename_pattern,
        filename
    )
    annotation_matched = re.search(
        annotation_filename_pattern,
        filename
    )
    return sensor_matched is not None or annotation_matched is not None


def get_pid(filepath):
    if is_mhealth_filepath(filepath):
        matched = re.search(MHEALTH_FILEPATH_PATTERN, filepath)
    elif is_mhealth_flat_filepath(filepath):
        matched = re.search(MHEALTH_FLAT_FILEPATH_PATTERN, filepath)
    else:
        return None
    return matched.group(1) if matched is not None else None


def get_sensor_type(filepath):
    assert is_mhealth_filename(filepath)
    filename = os.path.basename(filepath)
    result = filename.split('.')[0].split('-')[0]
    return result


def get_data_type(filepath):
    assert is_mhealth_filename(filepath)
    filename = os.path.basename(filepath)
    tokens = filename.split('.')[0]
    tokens = tokens.split('-')
    if len(tokens) >= 2:
        return tokens[1]
    else:
        return None


def get_version_code(filepath):
    assert is_mhealth_filename(filepath)
    filename = os.path.basename(filepath)
    tokens = filename.split('.')[0]
    tokens = tokens.split('-')
    if len(tokens) >= 3:
        return tokens[2]
    else:
        return None


def get_sid(filepath):
    assert is_mhealth_filename(filepath)
    filename = os.path.basename(filepath)
    return filename.split('.')[1].split('-')[0]


def get_file_type(filepath):
    assert is_mhealth_filename(filepath)
    filename = os.path.basename(filepath)
    return filename.split('.')[-2]


def get_file_timestamp(filepath):
    assert is_mhealth_filename(filepath)
    filename = os.path.basename(filepath)
    timestamp_str = filename.split('.')[-3]
    timestamp_str = timestamp_str.replace('M', '-').replace('P', '+')
    return datetime.strptime(timestamp_str, '%Y-%m-%d-%H-%M-%S-%f-%z')


def get_timezone_name(filepath):
    dt = get_file_timestamp(filepath)
    return dt.strftime('%Z')


