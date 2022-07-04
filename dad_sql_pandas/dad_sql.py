import pandas as pd

def load(vm, da):
    df = pd.DataFrame(**da._asdict())
    return df

def select(vm, da): return da
