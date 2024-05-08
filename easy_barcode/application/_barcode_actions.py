from pyguiadapter.ui import ExecutionContext, ActionItem

from ._common_actions import COMMON_MENUS, action_load_configs, action_save_configs
from ._constants import *

# 序列化时需忽略的键
_IGNORED_KEYS = []


def _on_save_barcode_configs(ctx: ExecutionContext):
    action_save_configs(
        ctx,
        dialog_title=SAVE_CONFIGS_DIALOG_TITLE,
        file_filters=FILE_FILTER_BARCODE_CONFIGS,
        ignored_keys=_IGNORED_KEYS,
    )


def _on_load_barcode_configs(ctx: ExecutionContext):
    action_load_configs(
        ctx,
        dialog_title=LOAD_CONFIGS_DIALOG_TITLE,
        file_filters=FILE_FILTER_BARCODE_CONFIGS,
        ignored_keys=_IGNORED_KEYS,
    )


_action_load = ActionItem(
    text=ACTION_LOAD_CONFIGS,
    callback=_on_load_barcode_configs,
    shortcut=SHORTCUT_LOAD_CONFIGS,
)

_action_save = ActionItem(
    text=ACTION_SAVE_CONFIGS,
    callback=_on_save_barcode_configs,
    shortcut=SHORTCUT_SAVE_CONFIGS,
)


BARCODE_MENUS = {
    MENU_FILE: {
        ACTION_SAVE_CONFIGS: _action_save,
        ACTION_LOAD_CONFIGS: _action_load,
    },
    **COMMON_MENUS,
}
