from .. import dataset


def test_is_mhealth_filepath():
    correct_test_cases = [
        'D:\\data\\spades_lab\\SPADES_7\\MasterSynced\\2015\\11\\19\\16',
        'D:\\data\\spades_lab\\SPADES_7\\MasterSynced\\2015\\11\\19\\16\\',
        'D:/data/spades_lab/SPADES_7/MasterSynced/2015/11/19/16/',
        'D:/data/spades_lab/SPADES_7/Derived/2015/11/19/16/',
        'D:/data/spades_lab/SPADES_7/Derived/AllSensors/2015/11/19/16/',
        'D:/data/spades_lab/SPADES_7/MasterSynced/2015/11/19/16',
        '''D:/data/spades_lab/SPADES_7/MasterSynced/2015/11/19/16/
        ActigraphGT9X-AccelerationCalibrated-NA.TAS1E23150152-AccelerationCalibrated.
        2015-11-19-16-00-00-000-M0500.sensor.csv''',
    ]

    incorrect_test_cases = [
        'C:\\',
        'C:/',
        'D:/data/spades_lab/SPADES_7/MasterSynced/2015/16',
        'D:/data/spades_lab/SPADES_7/MasterSynced/20/16',
        'D:/data/spades_lab/SPADES_7/Mastenced/2015/16/17/21/'
    ]
    for test_case in correct_test_cases:
        assert dataset.is_mhealth_filepath(test_case)

    for test_case in incorrect_test_cases:
        assert not dataset.is_mhealth_filepath(test_case)


def test_is_mhealth_flat_filepath():
    correct_test_cases = [
        'D:\\data\\spades_lab\\SPADES_7\\MasterSynced\\asdf.csv',
        'D:\\data\\spades_lab\\SPADES_7\\MasterSynced\\adfa.csv',
        'D:/data/spades_lab/SPADES_7/MasterSynced/sdf.csv',
        'D:/data/spades_lab/SPADES_7/Derived/dfew.csv',
        'D:/data/spades_lab/SPADES_7/Derived/AllSensors/dfsd.csv',
        '''D:/data/spades_lab/SPADES_7/MasterSynced/ActigraphGT9X-AccelerationCalibrated-NA.TAS1E23150152-AccelerationCalibrated.2015-11-19-16-00-00-000-M0500.sensor.csv''',
    ]

    incorrect_test_cases = [
        'C:\\',
        'C:/',
        'D:/data/spades_lab/SPADES_7/MasterSyn/',
        'D:/data/spades_lab/SPADES_7/MasterSynced/20/16',
        'D:/data/spades_lab/SPADES_7/Mastenced/2015/16/17/21/',
        '''D:/data/spades_lab/SPADES_7/MasterSynced/2015/11/19/16/ActigraphGT9X-AccelerationCalibrated-NA.TAS1E23150152-AccelerationCalibrated.2015-11-19-16-00-00-000-M0500.sensor.csv'''
    ]
    for test_case in correct_test_cases:
        assert dataset.is_mhealth_flat_filepath(test_case)

    for test_case in incorrect_test_cases:
        assert not dataset.is_mhealth_flat_filepath(test_case)


def test_is_mhealth_filename():
    correct_test_cases = [
        'ActigraphGT9X-AccelerationCalibrated-NA.TAS1E23150152-AccelerationCalibrated.2015-11-19-16-00-00-000-M0500.sensor.csv',
        'SPADESInLab.diego-SPADESInLab.2015-11-19-16-00-00-000-M0500.annotation.csv',
        'SPADESInLab.DIEGO-SPADESInLab.2015-11-19-16-00-00-000-M0500.annotation.csv',
    ]

    incorrect_test_cases = [
        'ActigraphGT9X-AccelerationCalibrated-NA.TAS1E23150152-AccelerationCalibrated.2015-11-19-16-00-00-000-M0500.annotation.csv',
        'Actig?raphGT9X-AccelerationCalibrated-NA.TAS1E23150152-AccelerationCalibrated.2015-11-19-16-00-00-000-M0500.sensor.csv',
        'ActigraphGT9X-NA.TAS1E23150152-AccelerationCalibrated.2015-11-19-16-00-00-000-M0500.sensor.csv',
        'ActigraphGT9X-AccelerationCalibrated-0,1,2.TAS1E23150152-AccelerationCalibrated.2015-11-19-16-00-00-000-M0500.sensor.csv',
        'ActigraphGT9X-AccelerationCalibrated-NA.tas1E23150152-AccelerationCalibrated.2015-11-19-16-00-00-000-M0500.sensor.csv',
        'ActigraphGT9X-AccelerationCalibrated-NA.TAS1E23150152-AccelerationCalibrated.2015-0-000-M0500.sensor.csv',
        'SPADESInLab-sdfsdf.diego-SPADESInLab.2015-11-19-16-00-00-000-M0500.annotation.csv'
    ]

    for test_case in correct_test_cases:
        assert dataset.is_mhealth_filename(test_case)

    for test_case in incorrect_test_cases:
        assert not dataset.is_mhealth_filename(test_case)


def test_get_pid():
    correct_test_cases = [
        'D:\\data\\spades_lab\\SPADES_7\\MasterSynced\\2015\\11\\19\\16',
        'D:\\data\\spades_lab\\SPADES_7\\MasterSynced\\2015\\11\\19\\16\\',
        'D:/data/spades_lab/SPADES_7/MasterSynced/2015/11/19/16/',
        'D:/data/spades_lab/SPADES_7/Derived/2015/11/19/16/',
        'D:/data/spades_lab/SPADES_7/Derived/AllSensors/2015/11/19/16/',
        'D:/data/spades_lab/SPADES_7/MasterSynced/2015/11/19/16',
        '''D:/data/spades_lab/SPADES_7/MasterSynced/2015/11/19/16/
        ActigraphGT9X-AccelerationCalibrated-NA.TAS1E23150152-AccelerationCalibrated.
        2015-11-19-16-00-00-000-M0500.sensor.csv''',
        'D:\\data\\spades_lab\\SPADES_7\\MasterSynced\\asdf.csv',
        'D:\\data\\spades_lab\\SPADES_7\\MasterSynced\\adfa.csv',
        'D:/data/spades_lab/SPADES_7/MasterSynced/sdf.csv',
        'D:/data/spades_lab/SPADES_7/Derived/dfew.csv',
        'D:/data/spades_lab/SPADES_7/Derived/AllSensors/dfsd.csv',
        '''D:/data/spades_lab/SPADES_7/MasterSynced/ActigraphGT9X-AccelerationCalibrated-NA.TAS1E23150152-AccelerationCalibrated.2015-11-19-16-00-00-000-M0500.sensor.csv'''
    ]

    incorrect_test_cases = [
        'C:\\',
        'C:/',
        'D:/data/spades_lab/SPADES_7/MasterSynced/2015/16',
        'D:/data/spades_lab/SPADES_7/MasterSynced/20/16',
        'D:/data/spades_lab/SPADES_7/Mastenced/2015/16/17/21/'
    ]

    for test_case in correct_test_cases:
        assert dataset.get_pid(test_case) == 'SPADES_7'

    for test_case in incorrect_test_cases:
        assert dataset.get_pid(test_case) is None


def test_get_sensor_type():
    correct_test_cases = [
        'ActigraphGT9X-AccelerationCalibrated-NA.TAS1E23150152-AccelerationCalibrated.2015-11-19-16-00-00-000-M0500.sensor.csv',
        'SPADESInLab.diego-SPADESInLab.2015-11-19-16-00-00-000-M0500.annotation.csv',
        'SPADESInLab.DIEGO-SPADESInLab.2015-11-19-16-00-00-000-M0500.annotation.csv',
    ]

    for test_case in correct_test_cases:
        print(test_case)
        assert dataset.get_sensor_type(test_case) == 'ActigraphGT9X' or dataset.get_sensor_type(test_case) == 'SPADESInLab'

def test_get_data_type():
    sensor_test_cases = [
        'ActigraphGT9X-AccelerationCalibrated-NA.TAS1E23150152-AccelerationCalibrated.2015-11-19-16-00-00-000-M0500.sensor.csv',
    ]

    annotation_test_cases = [
        'SPADESInLab.diego-SPADESInLab.2015-11-19-16-00-00-000-M0500.annotation.csv',
        'SPADESInLab.DIEGO-SPADESInLab.2015-11-19-16-00-00-000-M0500.annotation.csv',
    ]

    for test_case in sensor_test_cases:
        assert dataset.get_data_type(test_case) == 'AccelerationCalibrated'
    
    for test_case in annotation_test_cases:
        assert dataset.get_data_type(test_case) is None

def test_get_version_code():
    sensor_test_cases = [
        'ActigraphGT9X-AccelerationCalibrated-NA.TAS1E23150152-AccelerationCalibrated.2015-11-19-16-00-00-000-M0500.sensor.csv',
    ]

    annotation_test_cases = [
        'SPADESInLab.diego-SPADESInLab.2015-11-19-16-00-00-000-M0500.annotation.csv',
        'SPADESInLab.DIEGO-SPADESInLab.2015-11-19-16-00-00-000-M0500.annotation.csv',
    ]

    for test_case in sensor_test_cases:
        assert dataset.get_version_code(test_case) == 'NA'
    
    for test_case in annotation_test_cases:
        assert dataset.get_version_code(test_case) is None

    
def test_get_sid():
    sensor_test_cases = [
        'ActigraphGT9X-AccelerationCalibrated-NA.TAS1E23150152-AccelerationCalibrated.2015-11-19-16-00-00-000-M0500.sensor.csv',
    ]

    annotation_test_cases = [
        'SPADESInLab.diego-SPADESInLab.2015-11-19-16-00-00-000-M0500.annotation.csv',
        'SPADESInLab.DIEGO-SPADESInLab.2015-11-19-16-00-00-000-M0500.annotation.csv',
    ]

    for test_case in sensor_test_cases:
        assert dataset.get_sid(test_case) == 'TAS1E23150152'
    
    for test_case in annotation_test_cases:
        assert dataset.get_sid(test_case).lower() == 'diego'


def test_get_file_type():
    sensor_test_cases = [
        'ActigraphGT9X-AccelerationCalibrated-NA.TAS1E23150152-AccelerationCalibrated.2015-11-19-16-00-00-000-M0500.sensor.csv',
    ]

    annotation_test_cases = [
        'SPADESInLab.diego-SPADESInLab.2015-11-19-16-00-00-000-M0500.annotation.csv',
        'SPADESInLab.DIEGO-SPADESInLab.2015-11-19-16-00-00-000-M0500.annotation.csv',
    ]

    for test_case in sensor_test_cases:
        assert dataset.get_file_type(test_case) == 'sensor'
    
    for test_case in annotation_test_cases:
        assert dataset.get_file_type(test_case) == 'annotation'


def test_get_file_timestamp():
    from datetime import datetime
    sensor_test_cases = [
        'ActigraphGT9X-AccelerationCalibrated-NA.TAS1E23150152-AccelerationCalibrated.2015-11-19-16-00-00-000-M0500.sensor.csv',
    ]

    annotation_test_cases = [
        'SPADESInLab.diego-SPADESInLab.2015-11-19-16-00-00-000-M0500.annotation.csv',
        'SPADESInLab.DIEGO-SPADESInLab.2015-11-19-16-00-00-000-M0500.annotation.csv',
    ]

    for test_case in sensor_test_cases:
        assert dataset.get_file_timestamp(test_case).timestamp() == 1447966800.0
    
    for test_case in annotation_test_cases:
        assert dataset.get_file_timestamp(test_case).timestamp() == 1447966800.0

def test_get_timezone_name():
    from datetime import datetime
    sensor_test_cases = [
        'ActigraphGT9X-AccelerationCalibrated-NA.TAS1E23150152-AccelerationCalibrated.2015-11-19-16-00-00-000-M0500.sensor.csv',
    ]

    annotation_test_cases = [
        'SPADESInLab.diego-SPADESInLab.2015-11-19-16-00-00-000-M0500.annotation.csv',
        'SPADESInLab.DIEGO-SPADESInLab.2015-11-19-16-00-00-000-M0500.annotation.csv',
    ]

    for test_case in sensor_test_cases:
        assert dataset.get_timezone_name(test_case) == 'UTC-05:00'
    
    for test_case in annotation_test_cases:
        assert dataset.get_timezone_name(test_case) == 'UTC-05:00'
