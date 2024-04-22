import os.path

from barcode import get_barcode_class
from barcode.writer import SVGWriter, ImageWriter

from easy_barcode.common.encoder import BaseEncoder
from ._constants import *


class BarcodeEncoder(BaseEncoder):
    def __init__(self, verbose: bool = True):
        super().__init__(verbose=verbose)

    def encode(
        self,
        *,
        barcode_type: str = None,
        code: str = None,
        dest_path: str = None,
        target_filename: str = None,
        text: str = None,
        preview_only: bool = None,
        overwrite_behavior: str = None,
        extra_args: dict = None,
        dpi: int = None,
        compress: bool = None,
        module_width: float = None,
        module_height: float = None,
        quiet_zone: float = None,
        font_path: str = None,
        font_size: int = None,
        text_distance: float = None,
        background: Color = None,
        foreground: Color = None,
        center_text: bool = None,
        verbose: bool = None,
    ):
        super().encode(
            code=code,
            preview_only=preview_only,
            dest_path=dest_path,
            target_filename=target_filename,
            overwrite_behavior=overwrite_behavior,
            verbose=verbose,
        )

        if extra_args is None:
            extra_args = {}
        if "writer" in extra_args:
            del extra_args["writer"]

        if background is None:
            background = DEFAULT_VALUE_BACKGROUND

        if foreground is None:
            foreground = DEFAULT_VALUE_FOREGROUND

        _, ext = os.path.splitext(target_filename)
        is_svg_file = ext.lower() == ".svg"

        if not is_svg_file and compress:
            self.warning(MSG_COMPRESS_IGNORED)
            compress = None

        if is_svg_file and not dpi:
            self.warning(MSG_DPI_IGNORED)

        if is_svg_file:
            writer = SVGWriter()
        else:
            writer = ImageWriter()

        barcode_class = get_barcode_class(barcode_type)
        output_filepath = os.path.abspath(os.path.join(dest_path, target_filename))
        with self.open_target_file(output_filepath, preview_only) as fp:
            options = {}
            self.add_options_to(
                options,
                dpi=dpi,
                compress=compress,
                module_width=module_width,
                module_height=module_height,
                quiet_zone=quiet_zone,
                font_path=font_path,
                font_size=font_size,
                text_distance=text_distance,
                background=background.to_hex_string(with_alpha=False),
                foreground=foreground.to_hex_string(with_alpha=False),
                center_text=center_text,
            )
            ins = barcode_class(code, writer=writer, **extra_args)
            ins.write(fp, text=text, options=options)
            if preview_only:
                result = fp
            else:
                result = output_filepath
            self.print_result(result, preview_only)
