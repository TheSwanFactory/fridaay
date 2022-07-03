import os,sys,yaml
from .constants import *

def read_yaml(name, folder=PIPE_FOLDER):
    filename = f'{name}.yml'
    path = os.path.join(folder, filename)
    with open(path, 'r') as file:
        yml = yaml.safe_load(file)
        return yml

def read_yamls(folder=PIPE_FOLDER):
    all = {}
    for root, dirs, files in os.walk(folder):
       print(f'read_yamls: {root}')
       for name in files:
          f = os.path.join(root, name)
          all[name] = f
    return all

def read_dad(dad):
    name = f'dad-{dad}'
    yml = read_yaml(name, DAD_FOLDER)
    return yml
