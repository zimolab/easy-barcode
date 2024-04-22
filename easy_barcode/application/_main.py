from pyguiadapter import GUIAdapter

from easy_barcode.barcode_1d import BarcodeEncoder, BARCODE_ENCODE_CONFIGS
from easy_barcode.barcode_1d import FUNC_NAME as BARCODE_ENCODE_FUNC_NAME
from easy_barcode.barcode_1d import FUNC_DESC as BARCODE_ENCODE_FUNC_DESC
from easy_barcode.qrcode_2d import FUNC_NAME as QRCODE_ENCODE_FUNC_NAME
from easy_barcode.qrcode_2d import FUNC_DESC as QRCODE_ENCODE_FUNC_DESC
from easy_barcode.qrcode_2d import QRCodeEncoder, QRCODE_ENCODE_CONFIGS


def apply_window_configs(gui_adapter: GUIAdapter):
    gui_adapter.selection_window_config.icon_mode = False

    gui_adapter.execution_window_config.show_func_result_dialog = False
    gui_adapter.execution_window_config.show_func_error_dialog = True
    gui_adapter.execution_window_config.print_func_error = False
    gui_adapter.execution_window_config.func_error_msg = "{}"

    gui_adapter.execution_window_config.print_func_start_msg = False
    gui_adapter.execution_window_config.print_func_finish_msg = False
    gui_adapter.execution_window_config.print_func_result = False


def main():
    barcode_encoder = BarcodeEncoder()
    qrcode_encoder = QRCodeEncoder()

    gui_adapter = GUIAdapter()
    apply_window_configs(gui_adapter)

    gui_adapter.add(
        barcode_encoder.encode,
        widget_configs=BARCODE_ENCODE_CONFIGS,
        display_name=BARCODE_ENCODE_FUNC_NAME,
        display_document=BARCODE_ENCODE_FUNC_DESC,
    )
    gui_adapter.add(
        qrcode_encoder.encode,
        widget_configs=QRCODE_ENCODE_CONFIGS,
        display_name=QRCODE_ENCODE_FUNC_NAME,
        display_document=QRCODE_ENCODE_FUNC_DESC,
    )

    gui_adapter.run()


if __name__ == "__main__":
    main()
