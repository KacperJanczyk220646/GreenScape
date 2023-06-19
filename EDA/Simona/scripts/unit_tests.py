import st_testing
import pandas as pd


path = 'EDA/Simona/scripts/Preprocessed_Dataset.csv'


def check_path():

    assert st_testing.path() == 'EDA/Simona/scripts/Preprocessed_Dataset.csv'
    print('right path')


def test_read_file_from_relative_path():

    file_path = 'EDA/Simona/scripts/Preprocessed_Dataset.csv'
    result = st_testing.read_file_from_relative_path(file_path)
    assert result is not None
    file_path = 'EDA/Simona/scripts/Preprocessed_Dataset.csv'
    assert isinstance(result, int)
    result = st_testing.read_file_from_relative_path(file_path)
    assert result is None


test_read_file_from_relative_path()
