from .constants import DAD_FOLDER
from .load import read_yamls
from .schema import Schema

class Registry:
    def __init__(self, folder=DAD_FOLDER):
        self.schemas = {}
        self.add_folder(folder)

    def add_dad(self, name, yml):
        for act, dad in yml.items():
            key = f'{name}.{act}'
            self.schemas[key] = Schema(act, dad)

    def add_folder(self, folder):
        ydict = read_yamls(folder)
        for id, yml in ydict.items():
            name = id.replace('dad-','')
            self.add_dad(name, yml)
