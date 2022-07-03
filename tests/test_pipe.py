import pytest
from .conftest import *

@pytest.fixture
def pipe():
    yml = read_yaml(TEST_FILE)
    p = Pipe(yml)
    return p

def test_pipe(pipe):
    assert pipe
