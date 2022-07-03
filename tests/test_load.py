import pytest
from .conftest import *

@pytest.fixture
def yml(): return load_yaml(TEST_FILE)

def test_yaml(yml):
    assert yml
    assert 'fridaay' in yml

def test_yamls():
    ydict = load_yamls()
    assert ydict
    assert TEST_FILE in ydict

def test_init(yml):
    action = yml['fridaay']
    assert TEST_DO == action['do']
