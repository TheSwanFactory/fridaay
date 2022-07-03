import pytest
from .conftest import *

@pytest.fixture
def pipe():
    yml = read_yaml(TEST_FILE)
    p = Pipe(yml)
    return p

def test_pipe(pipe):
    assert pipe

def test_find_dad(pipe):
    schema = pipe.find_dad('init')
    assert isinstance(schema, Schema)

def test_parse(pipe):
    schema = pipe.find_dad('init')
    assert isinstance(schema, Schema)
