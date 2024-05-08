from typing import Optional, Type

from qrcode.image.styles.colormasks import (
    QRColorMask,
    SolidFillColorMask,
    RadialGradiantColorMask,
    SquareGradiantColorMask,
    HorizontalGradiantColorMask,
    VerticalGradiantColorMask,
)

from easy_barcode.eenum import EEnum

SOLID_FILL = "SOLID_FILL"
RADIAL_GRADIENT = "RADIAL_GRADIENT"
SQUARE_RADIAL_GRADIENT = "SQUARE_RADIAL_GRADIENT"
HORIZONTAL_GRADIENT = "HORIZONTAL_GRADIENT"
VERTICAL_GRADIENT = "VERTICAL_GRADIENT"

_value_map = {
    SOLID_FILL: SolidFillColorMask,
    RADIAL_GRADIENT: RadialGradiantColorMask,
    SQUARE_RADIAL_GRADIENT: SquareGradiantColorMask,
    HORIZONTAL_GRADIENT: HorizontalGradiantColorMask,
    VERTICAL_GRADIENT: VerticalGradiantColorMask,
}


class ColorMask(EEnum):
    SolidFill = SOLID_FILL
    RadialGradient = RADIAL_GRADIENT
    SquareRadialGradient = SQUARE_RADIAL_GRADIENT
    HorizontalGradient = HORIZONTAL_GRADIENT
    VerticalGradient = VERTICAL_GRADIENT

    @classmethod
    def value_of(
        cls, value: str, default: Optional["ColorMask"] = None, raise_error: bool = True
    ) -> Optional["ColorMask"]:
        value = value.upper()
        return super().value_of(value, default, raise_error)

    def get_color_mask_class(self) -> Optional[Type[QRColorMask]]:
        return _value_map.get(self.value, None)
