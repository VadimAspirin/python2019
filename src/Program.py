import os
from UICatalog import UICatalog

CURRENT_FILE_DIR = os.path.dirname(__file__)
ROOT = os.path.dirname(CURRENT_FILE_DIR)
DATA_DIR = os.path.join(ROOT, 'data')
DATA_JSON_PATH = os.path.join(DATA_DIR, 'data.json')


if __name__ == "__main__":
    UICatalog(DATA_JSON_PATH).generate()