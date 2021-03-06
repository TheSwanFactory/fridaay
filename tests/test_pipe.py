import pytest
from .conftest import *

@pytest.fixture
def pipe():
    folder = path_resource(PKG_ID, PIPE_FOLDER)
    yml = load_yaml(DEMO_PIPE, folder)
    r = Registry()
    p = Pipe(r, yml)
    return p

def test_pipe(pipe):
    assert pipe

def test_compile(pipe):
    asms = pipe.compile()
    assert pipe.vars['SAPIENT']
    assert len(asms) == 2
    a0 = asms[0]
    assert a0.do == 'sql.load'
    a1 = asms[1]
    assert a1.from_key == a0.id

def test_run(pipe):
    vm = pipe.run()
    assert vm
    dp = vm.get(DEMO_PIPE)
    assert len(dp) == 2
    assert len(pipe.data[DEMO_PIPE]) == 2
