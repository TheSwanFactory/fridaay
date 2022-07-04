import pytest
from .conftest import *
from dad_sql_pandas import *
import pandas as pd

@pytest.fixture
def pipe():
    yml = load_yaml(TEST_FILE)
    r = Registry()
    p = Pipe(r, yml)
    return p

def test_pipe(pipe):
    assert pipe

def test_compile(pipe):
    asms = pipe.compile()
    assert pipe.vars['SAPIENT']
    print(asms)
    assert len(asms) == 2
    a0 = asms[0]
    assert a0.do == 'sql.load'
    a1 = asms[1]
    print(a1)
    assert a1.from_key == a0.id
