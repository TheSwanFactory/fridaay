from fridaay import K_FKEY
import pandas as pd

def load(vm, da):
    # Assume columns + data
    df = pd.DataFrame(**da._asdict())
    return df

def select(vm, da):
    df = vm.get(da.from_key)
    return df
