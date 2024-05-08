from PyQt6.QtWidgets import QApplication

from easy_barcode.res import get_res_file


SELECTION_WINDOW_TITLE = QApplication.tr("条形码生成器")
DOCUMENT_LABEL = QApplication.tr("功能说明")
FUNC_LIST_LABEL = QApplication.tr("功能列表")
PARAM_GROUPBOX_TITLE = QApplication.tr("参数设置")
AUTOCLEAR_CHECKBOX_TEXT = QApplication.tr("自动清空输出")
OUTPUT_DOCK_TITLE = QApplication.tr("输出")
DOCUMENT_DOCK_TITLE = QApplication.tr("功能说明")
ERROR_DIALOG_TITLE = QApplication.tr("错误")
INFO_DIALOG_TITLE = QApplication.tr("提示")
SAVE_CONFIGS_DIALOG_TITLE = QApplication.tr("保存配置")
LOAD_CONFIGS_DIALOG_TITLE = QApplication.tr("加载配置")
CONFIGS_SAVED_MESSAGE = QApplication.tr("配置已保存至：{}")
FILE_NOT_FOUND_MESSAGE = QApplication.tr("文件不存在：{}")

BUTTON_SELECTION_FUNC = QApplication.tr("选择")
BUTTON_EXECUTE_FUNC = QApplication.tr("执行")
BUTTON_CLEAR_OUTPUT = QApplication.tr("清空输出")

APP_STYLE_WINDOWS = None

WINDOW_ICON_FILE = get_res_file("icon.png")
BARCODE_ICON_FILE = get_res_file("barcode.svg")
QRCODE_ICON_FILE = get_res_file("qrcode.svg")

APP_NAME = QApplication.tr("简易条形码生成器")
APP_DESCRIPTION = QApplication.tr(
    "一个简单的条形码生成器，可以生成各种条形码、二维码，支持保存生成和加载生成配置、批量生成等功能。"
)
APP_LOGO_FILE = "logo.png"
APP_VERSION = "0.0.1"
APP_AUTHOR = "zimolab"
APP_REPO_URL = "https://github.com/zimolab/easy-barcode"
APP_LICENSE = "GPL 3.0"

LICENSE_FILE = "License"

MENU_FILE = QApplication.tr("文件")
MENU_ABOUT = QApplication.tr("关于")
MENU_VIEWS = QApplication.tr("视图")

ACTION_SAVE_CONFIGS = QApplication.tr("保存配置")
ACTION_LOAD_CONFIGS = QApplication.tr("加载配置")
ACTION_ABOUT = QApplication.tr("关于")
ACTION_HELP = QApplication.tr("帮助")
ACTION_LICENSE = QApplication.tr("开源许可")

ACTION_SHOW_DOCUMENT_DOCK = QApplication.tr("显示功能说明视图")
ACTION_SHOW_OUTPUT_DOCK = QApplication.tr("显示输出视图")

SHORTCUT_SAVE_CONFIGS = "Ctrl+S"
SHORTCUT_LOAD_CONFIGS = "Ctrl+L"

FILE_EXT_BARCODE_CONFIGS = ".barcode"
FILE_EXT_QRCODE_CONFIGS = ".qrcode"

FILE_FILTER_BARCODE_CONFIGS = QApplication.tr(
    "条形码配置文件 (*{0})".format(FILE_EXT_BARCODE_CONFIGS)
)

FILE_FILTER_QRCODE_CONFIGS = QApplication.tr(
    "二维码配置文件 (*{0})".format(FILE_EXT_QRCODE_CONFIGS)
)


HELP_PAGE_URL = APP_REPO_URL
