from .conftest import *

def test_yaml():
    yml = read_yaml(TEST_FILE)
    assert yml
    #assert 'init' in yml
