from collections import namedtuple
import dad_sql_pandas as sql
import pandas as pd

def tuplify(name, d): return namedtuple(name, d.keys())(**d)

TEST_DATA = {
    "columns": ["A", "B"],
    "data": [[1,2],[11,12],[21,22]]
}

TEST_DF = "test_data"
TEST_SELECT= {
    "from_key": TEST_DF
}

def test_pandas():
    df = pd.DataFrame()
    assert df.empty

def test_create():
    columns = ['A','B']
    df = pd.DataFrame(**TEST_DATA)
    assert not df.empty

def test_tuple():
    da = tuplify("TEST_DATA", TEST_DATA)
    assert da.columns == TEST_DATA["columns"]

def test_load():
    da = tuplify("TEST_DATA", TEST_DATA)
    df = sql.load(True, da)
    assert not df.empty

def test_select():
    da = tuplify("TEST_DATA", TEST_DATA)
    db = tuplify("TEST_SELECT", TEST_SELECT)
    df = sql.load(True, da)
    vm = {TEST_DF: df}
    df2 = sql.select(vm, db)
    assert not df2.empty
