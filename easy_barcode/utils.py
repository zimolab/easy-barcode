import json
import platform
from typing import Optional, List

from PyQt6.QtWidgets import QStyleFactory


def safe_del(obj: dict, *keys: str):
    if not keys:
        return
    for key in keys:
        if key in obj:
            del obj[key]


def is_windows() -> bool:
    system_name = platform.system().lower()
    return system_name.startswith("windows")


def get_app_style(default_style: str) -> Optional[str]:
    if is_windows() and default_style in QStyleFactory.keys():
        return default_style
    return None


def dump_json(obj: dict, filepath: str, ignored_keys: List[str] = None):
    copied = obj.copy()
    safe_del(copied, *ignored_keys)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(copied, f, indent=4, ensure_ascii=False)


def load_json(filepath: str, ignored_key: List[str] = None) -> dict:
    with open(filepath, "r", encoding="utf-8") as f:
        obj = json.load(f)
    if ignored_key:
        safe_del(obj, *ignored_key)
    return obj
