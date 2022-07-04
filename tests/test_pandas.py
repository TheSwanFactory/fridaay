import pandas as pd
from dad_sql_pandas import *

def test_pandas():
    df = pd.DataFrame()
    assert df.empty

def test_create():
    columns = ['A','B']
    data = [[1,2],[11,12],[21,22]]
    df = pd.DataFrame(data=data, columns=columns)
    assert not df.empty
