import pytest
from .conftest import *
import datetime
import importlib.resources

@pytest.fixture
def yml():
    folder = path_resource(PKG_ID, PIPE_FOLDER)
    yml = load_yaml(TEST_FILE, folder)
    return yml

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
    path = path_package(PKG_NAME)
    assert PKG_NAME in str(path)

def test_resource():
    path = path_resource(PKG_NAME, 'dad')
    assert PKG_NAME in path
    assert 'dad' in path
