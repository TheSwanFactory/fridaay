import pytest
from .conftest import *

@pytest.fixture
def yml():
    yml = read_yaml(TEST_FILE)
    return yml

def test_yaml(yml):
    assert yml
    assert 'fridaay' in yml

def test_yamls():
    ydict = read_yamls()
    assert ydict
    assert TEST_FILE in ydict

def test_init(yml):
    action = yml['fridaay']
    assert TEST_DO == action['do']
