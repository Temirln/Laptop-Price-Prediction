import os

from backend.settings import BASE_DIR

def get_full_path(path):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(BASE_DIR, path)
    return filename