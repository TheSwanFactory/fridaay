from collections import namedtuple
from dad_sql_pandas import *
import pandas as pd

TEST_DATA = {
    "columns": ["A", "B"],
    "data": [[1,2],[11,12],[21,22]]
}

def test_pandas():
    df = pd.DataFrame()
    assert df.empty

def test_create():
    columns = ['A','B']
    df = pd.DataFrame(**TEST_DATA)
    assert not df.empty

def test_tuple():
    cols = TEST_DATA["columns"]
    data = TEST_DATA["data"]
    struct = namedtuple("TEST_DATA", cols)
