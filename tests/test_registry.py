import pytest
from .conftest import *

@pytest.fixture
def reg(): return Registry()
@pytest.fixture
def yml(): return read_yaml(TEST_FILE)

def test_registry(reg):
    assert reg
    assert TEST_DO in reg.schemas

def test_schema(reg):
    schema = reg.schemas[TEST_DO]
    assert schema

def test_dadify(reg, yml):
    init = yml[FIRST_ID]
    assert init
    init['id'] = FIRST_ID
    dad = reg.dadify(init)
    assert dad.id == FIRST_ID
    imp = dad.imports
    assert imp
    assert reg.load(imp)
