from .constants import *
from .schema import Schema

class Pipe:
    def __init__(self, reg, yml):
        self.registry = reg
        self.source = yml
        self.object = []
        self.schemas = {}
        self.next_index = 0
        self.vars = {K_VAR: FIRST_ID}

    def substitute(self, action):
        for key, value in action.items():
            if value[0] == K_VAR: action[key] = self.vars[1:]

    def compile(self):
        for id, action in self.source.items():
            action['id'] = id
            self.substitute(action)
            act = action['do']
            schema = self.find_dad(act)
            obj = schema.parse(action)
            self.object.push(obj)
            self.vars[K_VAR] = id

    def find_dad(self, act):
        if act not in self.schemas:
            yml = read_dad(act)
            schema = Schema(act, yml)
            self.schemas[act] = schema
        return self.schemas[act]
