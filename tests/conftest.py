import os
import sys
PKG_NAME='fridaay'
TEST_FILE="demo_pets"
TEST_DO='core.init'
TEST_ID='test_data'

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
    '.', f'./{PKG_NAME}', '..', f'../{PKG_NAME}'
)))

from fridaay import *
