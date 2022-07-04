import pandas as pd
from dad_sql_pandas import *

PDATA = {
    "columns": ["A", "B"],
    "data": [[1,2],[11,12],[21,22]]
}

def test_pandas():
    df = pd.DataFrame()
    assert df.empty

def test_create():
    columns = ['A','B']
    df = pd.DataFrame(**PDATA)
    assert not df.empty
