import pytest
from .conftest import *

@pytest.fixture
def reg(): return Registry()
@pytest.fixture
def yml(): return load_yaml(TEST_FILE)

def test_registry(reg):
    assert reg
    assert TEST_DO in reg.schemas

def test_schema(reg):
    schema = reg.schemas[TEST_DO]
    assert schema

def test_assemble(reg, yml):
    init = yml[PKG_ID]
    assert init
    init['id'] = PKG_ID
    imp = init['imports']
    assert imp
    mods = reg.load(imp)
    assert mods

    action = yml[TEST_ID]
    action['id'] = TEST_ID
    assert action
    dad = reg.assemble(action)
    assert dad.id == TEST_ID
    assert dad.CODE
