from collections import namedtuple

class Schema:
    def __init__(self, act, dad):
        self.act = act
        self.dad = dad
        self.keys = self.sanitize(dad.keys())
        self.struct = namedtuple(self.act, self.keys)

    def sanitize(self, keys):
        return [k for k in keys]

    def parse(self, action):
        tuple = self.struct._make(action)
        return tuple
