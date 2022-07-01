import os,sys,yaml
PIPE_FOLDER="pipes"
DAD_FOLDER="fridaay/dad"

def read_yaml(filename, folder=PIPE_FOLDER):
    path = os.path.join(PIPE_FOLDER, filename)
    with open(path, 'r') as file:
        yml = yaml.safe_load(file)
        return yml

def read_schema(action):
    filename = f'dad-{action}'
    yml = read_yaml(filename, DAD_FOLDER)
    return yml
