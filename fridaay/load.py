import os,sys,yaml
from .constants import *

def read_yaml(name, folder=PIPE_FOLDER):
    filename = f'{name}.yml'
    path = os.path.join(folder, filename)
    with open(path, 'r') as file:
        yml = yaml.safe_load(file)
        return yml

def read_yamls(folder=PIPE_FOLDER):
    ydict = {}
    for root, dirs, files in os.walk(folder):
       print(f'read_yamls: {root}')
       for name in files:
          split = name.split('.')
          key = split[0]
          if 'yml' in split: ydict[key] = read_yaml(key, root)
    return ydict

def read_dad(dad):
    name = f'dad-{dad}'
    yml = read_yaml(name, DAD_FOLDER)
    return yml
