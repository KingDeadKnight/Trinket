import json
import os

def __init__(path):
    global datapath
    datapath = path
    target = open(str(path) + 'settings.json', 'w')
    config = """
    {
        \"port\": 19132,
        \"name\": \"A Minecraft: PE Server\"
    }
    """
    parsed = json.loads(config)
    target.write(json.dumps(parsed, indent=4, sort_keys=True))
    target.write(json.dumps(parsed, indent=4, sort_keys=True))


def generate_config():
    target = open(str(datapath) + 'settings.json', 'w')
    config = """
    {
        \"port\": 19132,
        \"name\": \"A Minecraft: PE Server\"
    }
    """
    parsed = json.loads(config)
    target.write(json.dumps(parsed, indent = 4, sort_keys = True))

def load_config():
    with open(datapath + 'settings.json', 'r') as handle:
        parsed = json.load(handle)
        return parsed

def getData():
    if os.path.isfile(datapath + 'settings.json'):
        return load_config()
    else:
        generate_config()
    return load_config()