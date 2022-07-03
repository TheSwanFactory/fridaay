import pytest
from .conftest import *

SCHEME = {
    "a": "STRING",
    "b": "STRING*"
}

DATA = {
    "id": "name",
    "do": "act",
    "a": "alpha",
    "b": "beta*"
}

@pytest.fixture
def schema():
    s = Schema('scheme', SCHEME)
    return s

def test_schema(schema):
    assert schema

def test_parse(schema):
    p = schema.parse(DATA)
    assert p
    assert p.a == DATA["a"]

def test_optional(schema):
    d = DATA.copy()
    d.pop("a")
    p = schema.parse(d)
    assert p
    assert p.a == False
    assert p.doc == False

def test_mandatory(schema):
    with pytest.raises(Exception) as e:
        d = DATA.copy()
        d.pop("b")
        print(d)
        p = schema.parse(d)
    print(e)

def test_base(schema):
    with pytest.raises(Exception) as e:
        d = DATA.copy()
        d.pop("do")
        p = schema.parse(d)
    print(e)
