import pytest
from .conftest import *

DICT = {
"a": "alpha",
"b": "beta"
}

def test_schema():
    schema = Schema('dict', DICT)
    assert schema

def test_parse():
    schema = Schema('dict', DICT)
    p = schema.parse(DICT)
    assert p
    assert p.a == DICT["a"]
