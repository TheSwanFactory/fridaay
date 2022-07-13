import pytest
from .conftest import *
import datetime
import importlib.resources

@pytest.fixture
def yml(): return load_yaml(TEST_FILE)

def test_yaml(yml):
    assert yml
    assert 'fridaay' in yml

def test_yamls():
    ydict = load_yamls()
    assert ydict
    assert TEST_FILE in ydict

def test_init(yml):
    action = yml['fridaay']
    assert TEST_DO == action['do']

def test_date(yml):
    action = yml['test_data']
    data = action['data']
    row = data[0]
    assert row[4] < datetime.date(2022, 1, 1)

def test_pkg_path():
    package_name = 'fridaay'
    path = load_pkg_path(package_name)
    assert package_name in str(path)
