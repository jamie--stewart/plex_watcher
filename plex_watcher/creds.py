import yaml
from os import path

CURRENT_DIR = path.abspath(path.dirname(__file__))
CREDS = path.join(CURRENT_DIR, "../creds.yml")

creds = {}


def get_creds():
    global creds
    if not creds:
        with open(CREDS, "r") as handle:
            creds = yaml.safe_load(handle)

    return creds
