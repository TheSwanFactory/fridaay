from .constants import *
from .schema import Schema

class Pipe:
    def __init__(self, reg, yml):
        self.registry = reg
        self.source = yml
        self.assembly = []
        self.next_index = 0
        self.vars = {K_VAR: FIRST_ID}

    def substitute(self, action):
        for key, value in action.items():
            if isinstance(value, str) and value[0] == K_VAR:
                var = value[1:]
                action[key] = self.vars[var]

    def init(self, asm):
        self.registry.load(asm.imports)
        return self

    def compile(self):
        for id, action in self.source.items():
            action['id'] = id
            self.substitute(action)
            asm = self.registry.assemble(action)
            if asm.do == K_INIT:
                self.init(asm)
            else:
                self.assembly.append(asm)
            self.vars[K_VAR] = id
        return self.assembly
