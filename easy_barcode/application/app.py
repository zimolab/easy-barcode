from pyguiadapter import GUIAdapter

from easy_barcode.barcode_1d import BarcodeEncoder, BARCODE_ENCODE_CONFIGS
from easy_barcode.barcode_1d import FUNC_NAME as BARCODE_ENCODE_FUNC_NAME
from easy_barcode.barcode_1d import FUNC_DESC as BARCODE_ENCODE_FUNC_DESC
from easy_barcode.qrcode_2d import FUNC_NAME as QRCODE_ENCODE_FUNC_NAME
from easy_barcode.qrcode_2d import FUNC_DESC as QRCODE_ENCODE_FUNC_DESC
from easy_barcode.qrcode_2d import QRCodeEncoder, QRCODE_ENCODE_CONFIGS

from ._constants import *
from .utils import get_app_style
from .barcode_actions import barcode_menus


def setup_windows(gui_adapter: GUIAdapter):
    # 配置Selection窗口
    gui_adapter.selection_window_config.icon_mode = False
    gui_adapter.selection_window_config.title = TEXT_SELECTION_WINDOW_TITLE
    gui_adapter.selection_window_config.select_button_text = BUTTON_SELECTION_FUNC
    gui_adapter.selection_window_config.document_label_text = TEXT_DOCUMENT_LABEL
    gui_adapter.selection_window_config.func_list_label_text = TEXT_FUNC_LIST_LABEL
    # 配置Execution窗口
    gui_adapter.execution_window_config.show_func_result_dialog = False
    gui_adapter.execution_window_config.show_func_error_dialog = True
    gui_adapter.execution_window_config.print_func_error = False
    gui_adapter.execution_window_config.func_error_msg = "{}"
    gui_adapter.execution_window_config.print_func_start_msg = False
    gui_adapter.execution_window_config.print_func_finish_msg = False
    gui_adapter.execution_window_config.print_func_result = False
    gui_adapter.execution_window_config.param_groupbox_title = TEXT_PARAM_GROUPBOX_TITLE
    gui_adapter.execution_window_config.execute_button_text = BUTTON_EXECUTE_FUNC
    gui_adapter.execution_window_config.clear_button_text = BUTTON_CLEAR_OUTPUT
    gui_adapter.execution_window_config.autoclear_checkbox_text = (
        TEXT_AUTOCLEAR_CHECKBOX
    )
    gui_adapter.execution_window_config.output_dock_config.title = (
        TEXT_OUTPUT_DOCK_TITLE
    )
    gui_adapter.execution_window_config.document_dock_config.title = (
        TEXT_DOCUMENT_DOCK_TITLE
    )
    gui_adapter.execution_window_config.func_error_dialog_title = (
        TEXT_ERROR_DIALOG_TITLE
    )
    gui_adapter.execution_window_config.enable_menubar_actions = True


def start():
    barcode_encoder = BarcodeEncoder()
    qrcode_encoder = QRCodeEncoder()

    gui_adapter = GUIAdapter(app_style=get_app_style())

    setup_windows(gui_adapter)

    gui_adapter.add(
        barcode_encoder.encode,
        widget_configs=BARCODE_ENCODE_CONFIGS,
        display_name=BARCODE_ENCODE_FUNC_NAME,
        display_document=BARCODE_ENCODE_FUNC_DESC,
        menus=barcode_menus,
        window_title=BARCODE_ENCODE_FUNC_NAME,
    )
    gui_adapter.add(
        qrcode_encoder.encode,
        widget_configs=QRCODE_ENCODE_CONFIGS,
        display_name=QRCODE_ENCODE_FUNC_NAME,
        display_document=QRCODE_ENCODE_FUNC_DESC,
        window_title=QRCODE_ENCODE_FUNC_NAME,
    )

    gui_adapter.run()
