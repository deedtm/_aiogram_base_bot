import os


def get_filename(path: str):
    return os.path.basename(path)


def get_dir_path(path: str):
    return os.path.dirname(path)


def get_dirname(path: str):
    return os.path.basename(get_dir_path(path))
