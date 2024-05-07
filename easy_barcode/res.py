import os.path
from importlib import resources


def get_res_dir() -> str:
    with resources.path("easy_barcode", "res") as res_dir:
        return str(res_dir)


def get_res_path(path: str) -> str:
    return os.path.join(get_res_dir(), path)


def get_res_file(filename: str) -> str:
    res_filepath = get_res_path(filename)
    if not os.path.isfile(res_filepath):
        raise FileNotFoundError(f"res file not found:{res_filepath}")
    return res_filepath
