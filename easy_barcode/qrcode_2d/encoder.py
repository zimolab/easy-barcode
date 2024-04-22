from typing import Type

from function2widgets import Color
from qrcode.image.styles.colormasks import QRColorMask

from easy_barcode.common.encoder import BaseEncoder


class QRCodeEncoder(BaseEncoder):

    def encode(
        self,
        *,
        code: str = None,
        preview_only: bool = None,
        dest_path: str = None,
        target_filename: str = None,
        overwrite_behavior: str = None,
        version: int = None,
        error_correction: str = None,
        optimize: int = None,
        box_size: int = None,
        border: int = None,
        fill_color: Color = None,
        back_color: Color = None,
        module_drawer: str = None,
        size_ratio: float = None,
        background_image_path: str = None,
        color_mask: Type[QRColorMask] = None,
        color_mask_colors: dict = None,
        embeded_image_path: str = None,
        verbose: bool = None,
    ):
        super().encode(
            code=code,
            preview_only=preview_only,
            dest_path=dest_path,
            target_filename=target_filename,
            overwrite_behavior=overwrite_behavior,
            verbose=verbose,
            **kwargs,
        )
