import pytest
from .conftest import *
import datetime
import importlib.resources

@pytest.fixture
def path(): return path_resource(PKG_ID, PIPE_FOLDER)

@pytest.fixture
def yml(path): return load_yaml(DEMO_PIPE, path)

def test_path(path):
    assert path
    assert PKG_ID in path

def test_yaml(yml):
    assert yml
    assert PKG_ID in yml

def test_yamls(path):
    ydict = load_yamls(path)
    assert ydict
    assert DEMO_PIPE in ydict

def test_init(yml):
    action = yml[PKG_ID]
    assert TEST_DO == action['do']

def test_date(yml):
    action = yml['test_data']
    data = action['data']
    row = data[0]
    assert row[4] < datetime.date(2022, 1, 1)

def test_pkg_path():
    path = path_package(PKG_ID)
    assert PKG_ID in str(path)

def test_resource():
    path = path_resource(PKG_ID, DAD_RESOURCE)
    assert PKG_ID in path
    assert DAD_RESOURCE in path
