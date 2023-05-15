import os

from backend.settings import BASE_DIR

def get_full_path(path):
    filename = os.path.join(BASE_DIR, path)
    return filename