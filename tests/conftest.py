import os
import sys
from fridaay import *

TEST_FILE="demo_pets"
TEST_DO='core.init'
TEST_ID='test_data'

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
    '.', f'./{PKG_ID}', '..', f'../{PKG_ID}'
)))
