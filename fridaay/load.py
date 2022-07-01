import os,sys,yaml
PIPE_FOLDER="pipes"
DAD_FOLDER="fridaay/dad"

def read_yaml(name, folder=PIPE_FOLDER):
    filename = f'{name}.yml'
    path = os.path.join(folder, filename)
    with open(path, 'r') as file:
        yml = yaml.safe_load(file)
        return yml

def read_dad(action):
    name = f'dad-{action}'
    yml = read_yaml(name, DAD_FOLDER)
    return yml
