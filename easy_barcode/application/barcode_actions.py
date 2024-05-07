import os.path

from function2widgets import Color
from pyguiadapter.ui import ExecutionContext, ActionItem

from ._constants import *
from .common_actions import COMMON_MENUS
from .utils import dump_json, load_json

# 序列化时需忽略的键
_IGNORED_KEYS = [
    "code",
    "target_filename",
]


def _serialization_preprocess(param_values: dict):
    for k, v in param_values.items():
        if isinstance(v, Color):
            param_values[k] = v.to_hex_string(with_alpha=False)


def _on_save_barcode_configs(ctx: ExecutionContext):
    config_filepath = ctx.get_save_file_path(
        title=TEXT_SAVE_CONFIGS_DIALOG_TITLE, filters=FILE_FILTER_BARCODE_CONFIGS
    )
    if not config_filepath:
        return
    current_param_values = ctx.get_param_values()
    _serialization_preprocess(current_param_values)
    try:
        dump_json(current_param_values, config_filepath, ignored_keys=_IGNORED_KEYS)
    except BaseException as e:
        ctx.show_critical_dialog(str(e), title=TEXT_ERROR_DIALOG_TITLE)
    else:
        ctx.show_info_dialog(
            TEXT_CONFIGS_SAVED_MESSAGE.format(os.path.abspath(config_filepath)),
            title=TEXT_INFO_DIALOG_TITLE,
        )


def _on_load_barcode_configs(ctx: ExecutionContext):
    config_filepath = ctx.get_open_file_path(
        title=TEXT_LOAD_CONFIGS_DIALOG_TITLE,
        filters=FILE_FILTER_BARCODE_CONFIGS,
    )
    if not config_filepath:
        return
    try:
        configs = load_json(config_filepath, ignored_key=_IGNORED_KEYS)
    except BaseException as e:
        ctx.show_critical_dialog(str(e), title=TEXT_ERROR_DIALOG_TITLE)
        return

    try:
        ctx.set_param_values(configs)
    except BaseException as e:
        ctx.show_critical_dialog(str(e), title=TEXT_ERROR_DIALOG_TITLE)


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


barcode_menus = {
    MENU_FILE: {ACTION_SAVE_CONFIGS: _action_save, ACTION_LOAD_CONFIGS: _action_load},
    **COMMON_MENUS,
}
