from .load import read_dad

class Schema:
    def __init__(self, dad):
        self.dad = dad

    def parse(self, action):
        return action
