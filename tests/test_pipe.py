import pytest
from .conftest import *

@pytest.fixture
def yml():
    yml = read_yaml(TEST_FILE)
    return yml

def test_pipe(yml):
    pipe = Pipe(yml)
    assert pipe
