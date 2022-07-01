import os,sys,yaml
PIPE_FOLDER="pipes"

def read_yaml(filename, folder=PIPE_FOLDER):
    path = os.path.join(PIPE_FOLDER, filename)
    with open(path, 'r') as file:
        yml = yaml.safe_load(file)
        return yml
