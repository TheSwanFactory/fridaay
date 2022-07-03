import pytest
from .conftest import *

@pytest.fixture
def reg():
    r = Registry(DAD_FOLDER)
    return r

def test_pipe(reg):
    assert reg
    assert 'dad-init.init' in reg.schemas
