import platform
from typing import Optional

from PyQt6.QtWidgets import QStyleFactory

from ._constants import APP_STYLE_WINDOWS


def is_windows() -> bool:
    system_name = platform.system().lower()
    return system_name.startswith("windows")


def get_app_style() -> Optional[str]:
    if is_windows() and APP_STYLE_WINDOWS in QStyleFactory.keys():
        return APP_STYLE_WINDOWS
    return None
