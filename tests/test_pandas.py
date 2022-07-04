from collections import namedtuple
import dad_sql_pandas as sql
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
    keys = TEST_DATA.keys()
    struct = namedtuple("TEST_DATA", keys)
    dad = struct(**TEST_DATA)
    assert dad.columns == TEST_DATA["columns"]
    sql.load(True, dad)