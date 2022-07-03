import pytest
from .conftest import *

@pytest.fixture
def pipe():
    yml = read_yaml(TEST_FILE)
    r = Registry()
    p = Pipe(r, yml)
    return p

def test_pipe(pipe):
    assert pipe
