import pytest
from .conftest import *

@pytest.fixture
def yml():
    yml = read_yaml(TEST_FILE)
    return yml

def test_yaml(yml):
    assert yml
    assert 'fridaay' in yml

def test_init(yml):
    action = yml['fridaay']
    assert 'init' == action['do']
