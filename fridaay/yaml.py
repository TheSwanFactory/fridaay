import os,sys,yaml
PIPE_FOLDER="pipes"

def read_yaml(filename, folder=PIPE_FOLDER):
    print(os.getcwd())
    path = os.path.join(os.getcwd(),PIPE_FOLDER, filename)
    with open(path, 'r') as file:
        yml = yaml.safe_load(file)
        return yml
