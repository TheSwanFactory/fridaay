from .constants import DAD_FOLDER
from .load import read_yamls
from .schema import Schema

class Registry:
    def __init__(self, folder=DAD_FOLDER):
        self.schemas = {}
        self.add(folder)

    def add(self, folder):
        ydict = read_yamls(folder)
        for id, yml in ydict.items():
            name = id.replace('dad-','')
            for act, dad in yml.items():
                self.schemas[f'{name}.{act}'] = Schema(act, dad)
