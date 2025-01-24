import json

def load_project(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
