from .constants import DAD_FOLDER
from .load import *
from .schema import Schema

class Registry:
    def __init__(self, folder=DAD_FOLDER):
        self.schemas = {}
        self.modules = {}
        self.add_folder(folder)

    def add_dad(self, name, yml):
        for act, dad in yml.items():
            key = f'{name}.{act}'
            self.schemas[key] = Schema(act, dad)

    def add_folder(self, folder):
        ydict = load_yamls(folder)
        for id, yml in ydict.items():
            name = id.replace('dad-','')
            self.add_dad(name, yml)

    def dadify(self, action):
        act = action['do']
        schema = self.schemas[act]
        obj = schema.parse(action)
        return obj

    def load(self, imports):
        for key, value in imports.items():
            self.modules[key] = load_module(value)
        return self.modules
