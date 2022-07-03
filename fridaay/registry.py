#from .constants import DAD_FOLDER
from .load import read_yamls
from .schema import Schema

class Registry:
    def __init__(self, folder):
        ydict = read_yamls(folder)
