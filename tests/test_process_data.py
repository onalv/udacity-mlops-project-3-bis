import os
from ml.data import clean_data


def test_clean_data():
    clean_data("data", "census.csv")

    assert os.path.isfile('./data/clean/census.csv')
