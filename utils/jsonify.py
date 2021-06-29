import json


def load_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def dump_json(data, path):
    with open(path) as f:
        json.dump(data, f, indent=4)
