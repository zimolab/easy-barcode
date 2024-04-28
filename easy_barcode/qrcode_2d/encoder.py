import os.path
from decimal import Decimal
from typing import Dict, Union, Type, List, Tuple, Optional

from PyQt6.QtGui import QColor
import qrcode
from qrcode.main import QRCode, GenericImage
from qrcode.image.svg import SvgPathImage
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import QRColorMask, ImageColorMask
from qrcode.image.styles.moduledrawers.base import QRModuleDrawer

from easy_barcode.common.encoder import BaseEncoder
from ._constants import *
from .module_drawer import ModuleDrawer


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
        module_drawer: str = None,
        size_ratio: float = None,
        background_image_path: str = None,
        color_mask: str = None,
        color_mask_colors: Dict[str, Union[Color, str]] = None,
        embeded_image_path: str = None,
        verbose: bool = None,
    ):
        # ----------------- 参数归一化和参数校验阶段 -------------------------- #
        super().encode(
            code=code,
            preview_only=preview_only,
            dest_path=dest_path,
            target_filename=target_filename,
            overwrite_behavior=overwrite_behavior,
            verbose=verbose,
        )

        self._check_target_file(target_filename, preview_only)

        if error_correction is None:
            error_correction = DEFAULT_VALUE_ERROR_CORRECTION

        error_correction_value = ITEMS_ERROR_CORRECTION.get(error_correction, None)
        if error_correction_value is None:
            msg = ERR_MSG_INVALID_ERROR_CORRECTION.format(error_correction)
            self.error(msg)
            raise ValueError(msg)

        if version is None:
            fit = True
        else:
            version = version or 1
            fit = False

        dest_path = self._get_dest_path(dest_path)

        optimize = optimize or 0

        if box_size is None:
            box_size = DEFAULT_VALUE_BOX_SIZE

        is_output_svg = target_filename.lower().endswith(".svg")
        if module_drawer is not None:
            module_drawer_class = self._get_module_drawer_class(
                module_drawer, is_output_svg
            )
        else:
            module_drawer_class = None

        if size_ratio is None or size_ratio <= 0:
            size_ratio = DEFAULT_VALUE_SIZE_RATIO

        if background_image_path is not None:
            background_image_path = background_image_path.strip()
            if not background_image_path:
                self.error(ERR_MSG_EMPTY_BACKGROUND_IMAGE_PATH)
                raise ValueError(ERR_MSG_EMPTY_BACKGROUND_IMAGE_PATH)
            if not os.path.isfile(background_image_path):
                self.error(ERR_MSG_BACKGROUND_IMAGE_NOT_FOUND)
                raise ValueError(ERR_MSG_BACKGROUND_IMAGE_NOT_FOUND)

        if background_image_path and color_mask:
            self.warning(MSG_COLOR_MASK_IGNORED)

        if color_mask is not None:
            color_mask_class = self._get_color_mask_class(color_mask)
        else:
            color_mask_class = None

        if not isinstance(color_mask_colors, (dict, type(None))):
            raise TypeError("color_mask_colors must be a dict of colors")

        color_mask_colors = color_mask_colors or DEFAULT_VALUE_COLOR_MASK_COLORS
        color_mask_colors = self._get_color_mask_colors(color_mask_colors)

        if embeded_image_path is not None:
            embeded_image_path = embeded_image_path.strip()
            if not embeded_image_path:
                self.error(ERR_MSG_EMPTY_EMBEDED_IMAGE_PATH)
                raise ValueError(ERR_MSG_EMPTY_EMBEDED_IMAGE_PATH)
            if not os.path.isfile(embeded_image_path):
                self.error(ERR_MSG_EMBEDED_IMAGE_NOT_FOUND)
                raise ValueError(ERR_MSG_EMBEDED_IMAGE_NOT_FOUND)

        # ----------------- 二维码生成阶段 -------------------------- #
        image_factory = self._get_img_factory(is_output_svg)
        module_drawer_ins = self._create_module_drawer(module_drawer_class, size_ratio)
        back_color = self._get_back_color(all_colors=color_mask_colors)

        if background_image_path:
            color_mask_ins = self._create_background_image_mask(
                background_image_path, back_color
            )
        else:
            required_colors = self._get_required_colors(color_mask, color_mask_colors)
            color_mask_ins = self._create_color_mask(color_mask_class, required_colors)
        qr_obj = QRCode(
            version=version,
            error_correction=error_correction_value,
            box_size=box_size,
            border=border,
        )
        qr_obj.add_data(code, optimize=optimize)
        qr_obj.make(fit=fit)
        options = {}
        self.add_options_to(
            options,
            image_factory=image_factory,
            module_drawer=module_drawer_ins,
            embeded_image_path=embeded_image_path,
            color_mask=color_mask_ins,
        )
        img: GenericImage = qr_obj.make_image(**options)
        output_filepath = os.path.join(dest_path, target_filename)
        with self.open_target_file(output_filepath, preview_only) as fp:
            img.save(fp)
            if preview_only:
                result = fp
            else:
                result = output_filepath
            self.print_result(result, preview_only)

    def _get_module_drawer_class(
        self, module_drawer_name: Union[str, ModuleDrawer], is_svg: bool = False
    ) -> Type[QRModuleDrawer]:
        if isinstance(module_drawer_name, ModuleDrawer):
            tmp = module_drawer_name.get_module_drawer(is_svg=is_svg)
            if tmp is None:
                msg = ERR_MSG_UNSUPPORTED_SVG_MODULE_DRAWER.format(module_drawer_name)
                self.error(msg)
                raise ValueError(msg)
            return tmp

        if module_drawer_name in ITEMS_MODULE_DRAWER:
            module_drawer_name = ITEMS_MODULE_DRAWER[module_drawer_name]

        tmp = ModuleDrawer.value_of(module_drawer_name, default=None, raise_error=False)
        if tmp is None:
            msg = ERR_MSG_UNSUPPORTED_MODULE_DRAWER.format(module_drawer_name)
            self.error(msg)
            raise ValueError(msg)
        tmp = tmp.get_module_drawer(is_svg)
        if tmp is None:
            msg = ERR_MSG_UNSUPPORTED_SVG_MODULE_DRAWER.format(module_drawer_name)
            self.error(msg)
            raise ValueError(msg)
        return tmp

    def _get_color_mask_class(self, name: Union[str, ColorMask]) -> Type[QRColorMask]:
        if isinstance(name, ColorMask):
            tmp = name.get_color_mask_class()
            if tmp is None:
                msg = ERR_MSG_UNKNOWN_COLOR_MASK.format(name)
                self.error(msg)
                raise ValueError(msg)
            return tmp
        if name in ITEMS_COLOR_MASK:
            name = ITEMS_COLOR_MASK[name]
        tmp = ColorMask.value_of(name, default=None, raise_error=False)
        if tmp is None:
            msg = ERR_MSG_UNKNOWN_COLOR_MASK.format(name)
            self.error(msg)
            raise ValueError(msg)
        tmp = tmp.get_color_mask_class()
        if tmp is None:
            msg = ERR_MSG_UNKNOWN_COLOR_MASK.format(name)
            self.error(msg)
            raise ValueError(msg)
        return tmp

    @staticmethod
    def _get_color_mask_colors(
        colors: Dict[str, Union[Color, str]]
    ) -> Dict[str, Color]:
        return {
            key: Color.from_string(value) if isinstance(value, str) else value
            for key, value in colors.items()
        }

    def _get_required_colors(
        self, color_mask_name: str, all_colors: Dict[str, Color]
    ) -> List[Tuple]:
        if color_mask_name is None:
            return []
        if color_mask_name in ITEMS_COLOR_MASK:
            color_mask_name = ITEMS_COLOR_MASK[color_mask_name]
        tmp = ColorMask.value_of(color_mask_name, default=None, raise_error=False)
        if tmp is None:
            msg = ERR_MSG_UNKNOWN_COLOR_MASK.format(name)
            self.error(msg)
            raise ValueError(msg)

        required_color_labels = COLOR_MASK_REQUIRED_COLOR_LABELS.get(tmp, None)
        if required_color_labels is None:
            msg = ERR_MSG_UNKNOWN_COLOR_MASK.format(name)
            self.error(msg)
            raise ValueError(msg)
        return [
            all_colors.get(label).to_rgb_tuple(with_alpha=False)
            for label in required_color_labels
        ]

    @staticmethod
    def _get_back_color(all_colors: Dict[str, Color]) -> Color:
        return all_colors.get(BACK_COLOR_LABEL, Color.from_string("white"))

    @staticmethod
    def _get_img_factory(output_svg: bool) -> Type[StyledPilImage]:
        if output_svg:
            return SvgPathImage
        return StyledPilImage

    @staticmethod
    def _create_color_mask(
        clazz: Optional[Type[QRColorMask]], colors: List[Tuple]
    ) -> Optional[QRColorMask]:
        if clazz is None:
            return None
        return clazz(*colors)

    @staticmethod
    def _create_background_image_mask(
        background_image_path: str, back_color: Color
    ) -> Optional[ImageColorMask]:
        if not background_image_path:
            return None
        return ImageColorMask(
            background_image_path, back_color.to_rgb_tuple(with_alpha=False)
        )

    @staticmethod
    def _create_module_drawer(
        clazz: Optional[Type[QRModuleDrawer]], size_ratio: float
    ) -> Optional[QRModuleDrawer]:
        if clazz is None:
            return None
        size_ratio = Decimal(size_ratio)
        if clazz in MODULE_DRAWERS_SUPPORT_SIZE_RATIO:
            return clazz(size_ratio=size_ratio)
        return clazz()

    @staticmethod
    def _check_target_file(target_filename: str, preview_only: bool):
        if preview_only:
            return
        tmp = os.path.basename(target_filename)
        _, ext = os.path.splitext(tmp)
        ext = ext.lower()
        if not ext.endswith(".svg") and not ext.endswith(".png"):
            msg = ERR_MSG_UNSUPPORTED_FILE_EXTENSION.format(ext)
            raise ValueError(msg)
