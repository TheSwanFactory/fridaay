from fridaay import K_FKEY
import pandas as pd

# Helper Functions

def _choose_cols(df, colmap):
    cols = list(colmap.keys())
    return df.loc[:, cols]

def _filter(df, conds, all=True):
    return df

# DAD Functions

def load(vm, da):
    # Assume columns + data
    df = pd.DataFrame(**da._asdict())
    return df

def select(vm, da):
    df = vm.get(da.from_key)
    if da.cols: df = _choose_cols(df, da.cols)
    if da.where_all: df = _filter(df, da.where_all, True)
    if da.where_any: df = _filter(df, da.where_any, False)

    return df
