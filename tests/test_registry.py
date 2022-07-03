import pytest
from .conftest import *

@pytest.fixture
def reg():
    r = Registry()
    return r

def test_registry(reg):
    assert reg
    assert TEST_DO in reg.schemas

def test_schema(reg):
    schema = reg.schemas[TEST_DO]
