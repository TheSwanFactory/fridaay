from .load import read_schema

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
            schema = self.fetch(act)
            obj = self.parse(action, schema)
            self.object.push(obj)

    def fetch(self, act):
        if act not in self.schemas:
            yml = read_schema(act)
            self.schemas[act] = yml
        return self.schemas[act]

    def parse(self, action, schema):
        return self
