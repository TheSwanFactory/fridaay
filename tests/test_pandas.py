import pandas as pd
from dad_sql_pandas import *

def test_pandas():
    df = pd.DataFrame()
    assert df.empty
