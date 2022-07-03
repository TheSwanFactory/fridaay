import pytest
from .conftest import *

@pytest.fixture
def reg():
    r = Registry()
    return r

def test_pipe(reg):
    assert reg
    assert 'core.init' in reg.schemas
