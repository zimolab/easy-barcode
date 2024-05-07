from PyQt6.QtWidgets import QApplication

TEXT_SELECTION_WINDOW_TITLE = QApplication.tr("条形码生成器")
TEXT_DOCUMENT_LABEL = QApplication.tr("功能说明")
TEXT_FUNC_LIST_LABEL = QApplication.tr("功能列表")
TEXT_PARAM_GROUPBOX_TITLE = QApplication.tr("参数设置")
TEXT_AUTOCLEAR_CHECKBOX = QApplication.tr("自动清空输出")
TEXT_OUTPUT_DOCK_TITLE = QApplication.tr("输出")
TEXT_DOCUMENT_DOCK_TITLE = QApplication.tr("功能说明")
TEXT_ERROR_DIALOG_TITLE = QApplication.tr("错误")
TEXT_INFO_DIALOG_TITLE = QApplication.tr("提示")
TEXT_SAVE_CONFIGS_DIALOG_TITLE = QApplication.tr("保存配置")
TEXT_LOAD_CONFIGS_DIALOG_TITLE = QApplication.tr("加载配置")
TEXT_CONFIGS_SAVED_MESSAGE = QApplication.tr("配置已保存至：{}")

BUTTON_SELECTION_FUNC = QApplication.tr("选择")
BUTTON_EXECUTE_FUNC = QApplication.tr("执行")
BUTTON_CLEAR_OUTPUT = QApplication.tr("清空输出")

APP_STYLE_WINDOWS = None

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
ACTION_SHOW_OUTPUT_DOCK = QApplication.tr("显示输出试图")

SHORTCUT_SAVE_CONFIGS = "Ctrl+S"
SHORTCUT_LOAD_CONFIGS = "Ctrl+L"

FILE_EXT_BARCODE_CONFIGS = ".barcode"

FILE_FILTER_ALL_FILES = QApplication.tr("所有文件 (*.*)")
FILE_FILTER_BARCODE_CONFIGS = QApplication.tr(
    "条形码配置文件 (*{0})".format(FILE_EXT_BARCODE_CONFIGS)
)


HELP_PAGE_URL = APP_REPO_URL
