import os


def get_root_path():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(dir_path)
