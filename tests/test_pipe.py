import pytest
from .conftest import *

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
    print(asms)
    assert len(asms) == 2
