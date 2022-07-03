import pytest
from .conftest import *

DICT = {
"a": "alpha",
"b": "beta*"
}

@pytest.fixture
def schema():
    s = Schema('dict', DICT)
    return s

def test_schema(schema):
    assert schema

def test_parse(schema):
    p = schema.parse(DICT)
    assert p
    assert p.a == DICT["a"]

def test_optional(schema):
    DICT.pop("a")
    p = schema.parse(DICT)
    assert p

def test_mandatory():
    with pytest.raises(Exception) as e:
        DICT.pop("b")
        print(DICT)
        p = schema.parse(DICT)
    print(e)
