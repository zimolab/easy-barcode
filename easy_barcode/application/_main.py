from pyguiadapter import GUIAdapter

from easy_barcode.barcode import BarcodeEncoder, BARCODE_ENCODE_CONFIGS


def apply_window_configs(gui_adapter: GUIAdapter):
    gui_adapter.execution_window_config.show_func_result_dialog = False
    gui_adapter.execution_window_config.show_func_error_dialog = True
    gui_adapter.execution_window_config.print_func_error = False
    gui_adapter.execution_window_config.func_error_msg = "{}"

    gui_adapter.execution_window_config.print_func_start_msg = False
    gui_adapter.execution_window_config.print_func_finish_msg = False
    gui_adapter.execution_window_config.print_func_result = False


def main():
    barcode_encoder = BarcodeEncoder()

    gui_adapter = GUIAdapter()
    apply_window_configs(gui_adapter)

    gui_adapter.add(barcode_encoder.encode, widget_configs=BARCODE_ENCODE_CONFIGS)
    gui_adapter.run()


if __name__ == "__main__":
    main()
