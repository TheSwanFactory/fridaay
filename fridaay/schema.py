from collections import namedtuple

class Schema:
    def __init__(self, act, dad):
        self.act = act
        self.dad = dad
        self.keys = dad.keys()
        self.struct = namedtuple(self.act, self.keys)

    def parse(self, action):
        return action
