#from .constants import DAD_FOLDER
from .load import read_yamls
from .schema import Schema

class Registry:
    def __init__(self, folder):
        self.schemas = {}
        ydict = read_yamls(folder)
        for id, yml in ydict.items():
            for act, dad in yml.items():
                self.schemas[f'schema.{id}.{act}'] = Schema(act, dad)
