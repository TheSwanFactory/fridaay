from collections import namedtuple
import json
from .constants import *

class Schema:
    def __init__(self, act, dad):
        self.act = act
        self.dad = dad
        self.keys = self.sanitize(dad.keys())
        self.struct = namedtuple(self.act, self.keys)
        self.struct.__doc__ = json.dumps(dad)

    def sanitize(self, keys):
        return [k if k != K_FROM else K_FKEY for k in keys]

    def default(self, action):
        for k in self.keys:
            if k not in action: action[k] = False
        return action

    def parse(self, action):
        if K_FROM in action: action[F_KEY] = action.pop(K_FROM)
        defaulted = self.default(action)
        tuple = self.struct(**defaulted)
        return tuple
