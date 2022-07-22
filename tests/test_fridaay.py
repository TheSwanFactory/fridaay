from fridaay import __version__
from .conftest import DEMO_PIPE

def test_version():
    assert __version__ == '0.1.0'

def test_conftest():
    assert 'demo' in DEMO_PIPE
