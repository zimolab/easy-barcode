from typing import Dict, Union, Any

from function2widgets import Color
from pyguiadapter.ui import ExecutionContext, ActionItem

from ._common_actions import COMMON_MENUS, action_save_configs, action_load_configs
from ._constants import (
    LOAD_CONFIGS_DIALOG_TITLE,
    SAVE_CONFIGS_DIALOG_TITLE,
    FILE_FILTER_QRCODE_CONFIGS,
    ACTION_LOAD_CONFIGS,
    SHORTCUT_LOAD_CONFIGS,
    ACTION_SAVE_CONFIGS,
    SHORTCUT_SAVE_CONFIGS,
    MENU_FILE,
)

_IGNORED_KEYS = []


def _color_to_str(color: Union[str, Color]) -> str:
    if isinstance(color, Color):
        return color.to_hex_string(with_alpha=False)
    else:
        return color


def _serialization_preprocessor(data: Dict[str, Any]) -> None:
    for key, value in data.items():
        if key == "color_mask_colors":
            data[key] = {k: _color_to_str(v) for k, v in value.items()}


def _on_save_qrcode_configs(ctx: ExecutionContext):
    action_save_configs(
        ctx,
        dialog_title=SAVE_CONFIGS_DIALOG_TITLE,
        file_filters=FILE_FILTER_QRCODE_CONFIGS,
        ignored_keys=_IGNORED_KEYS,
        serialization_preprocessors=[_serialization_preprocessor],
    )


def _on_load_qrcode_configs(ctx: ExecutionContext):
    action_load_configs(
        ctx,
        dialog_title=LOAD_CONFIGS_DIALOG_TITLE,
        file_filters=FILE_FILTER_QRCODE_CONFIGS,
        ignored_keys=_IGNORED_KEYS,
    )


_action_load = ActionItem(
    text=ACTION_LOAD_CONFIGS,
    callback=_on_load_qrcode_configs,
    shortcut=SHORTCUT_LOAD_CONFIGS,
)

_action_save = ActionItem(
    text=ACTION_SAVE_CONFIGS,
    callback=_on_save_qrcode_configs,
    shortcut=SHORTCUT_SAVE_CONFIGS,
)

QRCODE_MENUS = {
    MENU_FILE: {
        ACTION_SAVE_CONFIGS: _action_save,
        ACTION_LOAD_CONFIGS: _action_load,
    },
    **COMMON_MENUS,
}
