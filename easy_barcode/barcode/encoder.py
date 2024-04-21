from function2widgets import Color

from easy_barcode.common.encoder import BaseEncoder


class BarcodeEncoder(BaseEncoder):
    def __init__(self, verbose: bool = True):
        super().__init__(verbose=verbose)

    def encode(
        self,
        *,
        code: str = None,
        text: str = None,
        preview_only: bool = None,
        dest_path: str = None,
        target_filename: str = None,
        overwrite_behavior: str = None,
        barcode_type: str = None,
        dpi: int = None,
        compress: bool = None,
        module_width: float = None,
        module_height: float = None,
        quiet_zone: int = None,
        font_path: str = None,
        font_size: int = None,
        text_distance: float = None,
        background: Color = None,
        foreground: Color = None,
        center_text: bool = None,
        verbose: bool = None,
    ):
        """ """
        super().encode(
            code=code,
            preview_only=preview_only,
            dest_path=dest_path,
            target_filename=target_filename,
            overwrite_behavior=overwrite_behavior,
            verbose=verbose,
            **kwargs,
        )
