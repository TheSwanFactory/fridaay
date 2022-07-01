from .conftest import *

def test_yaml():
    print(os.getcwd())

    yml = read_yaml(TEST_FILE)
    assert yml
    #assert 'init' in yml
