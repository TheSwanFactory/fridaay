from collections import namedtuple
from .constants import *

class Schema:
    def __init__(self, act, dad):
        self.act = act
        self.dad = dad
        self.keys = self.sanitize(dad.keys())
        self.struct = namedtuple(self.act, self.keys)

    def sanitize(self, keys):
        return [k if k != K_FROM else K_FKEY for k in keys]

    def parse(self, action):
        if K_FROM in action: action[F_KEY] = action.pop(K_FROM)
        tuple = self.struct(**action)
        return tuple
