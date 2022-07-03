import pytest
from .conftest import *

@pytest.fixture
def reg(): return Registry()

def test_registry(reg):
    assert reg
    assert TEST_DO in reg.schemas

def test_schema(reg):
    schema = reg.schemas[TEST_DO]
    assert schema

def test_dadify(reg):
    assert reg
