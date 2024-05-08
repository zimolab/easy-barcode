import os.path
import webbrowser
from typing import List, Callable, Dict, Any

from function2widgets import Color
from pyguiadapter.interact.upopup import show_about_popup, show_license_popup
from pyguiadapter.ui import ExecutionContext, ActionItem

from easy_barcode.res import get_res_file
from ._constants import *
from ..utils import load_json, dump_json

_FN_SHOW_DOCUMENT_DOCK = "show_document_dock"
_FN_SHOW_OUTPUT_DOCK = "show_output_dock"


def _on_show_document_dock(ctx: ExecutionContext):
    ctx.invoke(_FN_SHOW_DOCUMENT_DOCK)


def _on_show_output_dock(ctx: ExecutionContext):
    ctx.invoke(_FN_SHOW_OUTPUT_DOCK)


# noinspection PyUnusedLocal
def _on_show_about_popup(ctx: ExecutionContext):
    show_about_popup(
        app_logo=get_res_file(APP_LOGO_FILE),
        app_name=f"<b>{APP_NAME}</b>",
        app_description=APP_DESCRIPTION,
        app_copyright=None,
        app_fields={
            QApplication.tr("版本"): APP_VERSION,
            QApplication.tr("作者"): APP_AUTHOR,
            QApplication.tr("许可"): APP_LICENSE,
            QApplication.tr("主页"): f"<a href='{APP_REPO_URL}'>{APP_REPO_URL}</a>",
        },
    )


# noinspection PyUnusedLocal
def _on_show_license_popup(ctx: ExecutionContext):
    with open(get_res_file(LICENSE_FILE), "r", encoding="utf-8") as f:
        license_text = f.read()
    show_license_popup(license_text, window_title=QApplication.tr("开源许可"))


# noinspection PyUnusedLocal
def _on_go_to_help_page(ctx: ExecutionContext):
    webbrowser.open_new_tab(HELP_PAGE_URL)


def _config_serialization_preprocess(param_values: dict):
    for k, v in param_values.items():
        if isinstance(v, Color):
            param_values[k] = v.to_hex_string(with_alpha=False)


def action_load_configs(
    ctx: ExecutionContext,
    dialog_title: str,
    file_filters: str,
    ignored_keys: List[str] = None,
):
    config_filepath = ctx.get_open_file_path(
        title=dialog_title,
        filters=file_filters,
    )
    if not config_filepath:
        return
    if not os.path.isfile(config_filepath):
        ctx.show_critical_dialog(FILE_NOT_FOUND_MESSAGE, title=ERROR_DIALOG_TITLE)
        return
    try:
        configs = load_json(config_filepath, ignored_key=ignored_keys)
    except BaseException as e:
        ctx.show_critical_dialog(str(e), title=ERROR_DIALOG_TITLE)
        return

    try:
        ctx.set_param_values(configs, ignore_exceptions=False)
    except BaseException as e:
        ctx.show_critical_dialog(str(e), title=ERROR_DIALOG_TITLE)


def action_save_configs(
    ctx: ExecutionContext,
    dialog_title: str,
    file_filters: str,
    ignored_keys: List[str] = None,
    serialization_preprocessors: List[Callable[[Dict[str, Any]], None]] = None,
):
    if ignored_keys is None:
        ignored_keys = []
    config_filepath = ctx.get_save_file_path(title=dialog_title, filters=file_filters)
    if not config_filepath:
        return
    current_param_values = ctx.get_param_values()
    _config_serialization_preprocess(current_param_values)
    if serialization_preprocessors:
        for preprocessor in serialization_preprocessors:
            preprocessor(current_param_values)
    try:
        dump_json(current_param_values, config_filepath, ignored_keys=ignored_keys)
    except BaseException as e:
        ctx.show_critical_dialog(str(e), title=ERROR_DIALOG_TITLE)
    else:
        ctx.show_info_dialog(
            CONFIGS_SAVED_MESSAGE.format(os.path.abspath(config_filepath)),
            title=INFO_DIALOG_TITLE,
        )


COMMON_MENUS = {
    MENU_VIEWS: {
        ACTION_SHOW_DOCUMENT_DOCK: ActionItem(
            ACTION_SHOW_DOCUMENT_DOCK, _on_show_document_dock
        ),
        ACTION_SHOW_OUTPUT_DOCK: ActionItem(
            ACTION_SHOW_OUTPUT_DOCK, _on_show_output_dock
        ),
    },
    MENU_ABOUT: {
        ACTION_ABOUT: ActionItem(ACTION_ABOUT, _on_show_about_popup),
        ACTION_HELP: ActionItem(ACTION_HELP, _on_go_to_help_page),
        ACTION_LICENSE: ActionItem(ACTION_LICENSE, _on_show_license_popup),
    },
}
