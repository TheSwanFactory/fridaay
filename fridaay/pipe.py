from .load import read_dad
from .schema import Schema

class Pipe:
    def __init__(self, yml):
        self.source = yml
        self.object = []
        self.schemas = {}
        self.next_index = 0

    def compile(self):
        for id, action in self.source.items():
            action['id'] = id
            act = action['do']
            schema = self.find_schema(act)
            obj = self.parse(action, schema)
            self.object.push(obj)

    def find_schema(self, act):
        if act not in self.schemas:
            yml = read_dad(act)
            schema = Schema(yml)
            self.schemas[act] = yml
        return self.schemas[act]

    def parse(self, action, schema):
        return self
