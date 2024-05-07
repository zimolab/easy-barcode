import webbrowser

from pyguiadapter.interact.upopup import show_about_popup, show_license_popup
from pyguiadapter.ui import ExecutionContext, ActionItem

from easy_barcode.res import get_res_file
from ._constants import *


def _action_show_document_dock(ctx: ExecutionContext):
    ctx.invoke("show_document_dock")


def _action_show_output_dock(ctx: ExecutionContext):
    ctx.invoke("show_output_dock")


def _action_show_about_popup(ctx: ExecutionContext):
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


def _action_show_license_popup(ctx: ExecutionContext):
    with open(get_res_file(LICENSE_FILE), "r", encoding="utf-8") as f:
        license_text = f.read()
    show_license_popup(license_text, window_title=QApplication.tr("开源许可"))


def _action_go_to_help_page(ctx: ExecutionContext):
    webbrowser.open_new_tab(HELP_PAGE_URL)


COMMON_MENUS = {
    MENU_VIEWS: {
        ACTION_SHOW_DOCUMENT_DOCK: ActionItem(
            ACTION_SHOW_DOCUMENT_DOCK, _action_show_document_dock
        ),
        ACTION_SHOW_OUTPUT_DOCK: ActionItem(
            ACTION_SHOW_OUTPUT_DOCK, _action_show_output_dock
        ),
    },
    MENU_ABOUT: {
        ACTION_ABOUT: ActionItem(ACTION_ABOUT, _action_show_about_popup),
        ACTION_HELP: ActionItem(ACTION_HELP, _action_go_to_help_page),
        ACTION_LICENSE: ActionItem(ACTION_LICENSE, _action_show_license_popup),
    },
}
