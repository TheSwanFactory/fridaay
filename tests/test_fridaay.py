from fridaay import __version__
from .conftest import TEST_FILE

def test_version():
    assert __version__ == '0.1.0'

def test_conftest():
    assert 'demo' in TEST_FILE
