from typing import Optional, Type, Dict, Tuple

from qrcode.image.styles.moduledrawers.base import QRModuleDrawer
from qrcode.image.styles.moduledrawers import (
    SquareModuleDrawer,
    CircleModuleDrawer,
    RoundedModuleDrawer,
    GappedSquareModuleDrawer,
    VerticalBarsDrawer,
    HorizontalBarsDrawer,
)
from qrcode.image.styles.moduledrawers.svg import (
    SvgPathSquareDrawer,
    SvgPathCircleDrawer,
)
from easy_barcode.eenum import EEnum

SQUARE = "SQUARE"
ROUNDED = "ROUNDED"
CIRCLE = "CIRCLE"
GAPPED = "GAPPED"
VERTICAL_BARS = "VERTICAL_BARS"
HORIZONTAL_BARS = "HORIZONTAL_BARS"


_value_map: Dict[str, Tuple[QRModuleDrawer, Optional[QRModuleDrawer]]] = {
    SQUARE: (SquareModuleDrawer, SvgPathSquareDrawer),
    ROUNDED: (RoundedModuleDrawer, None),
    CIRCLE: (CircleModuleDrawer, SvgPathCircleDrawer),
    GAPPED: (GappedSquareModuleDrawer, None),
    VERTICAL_BARS: (VerticalBarsDrawer, None),
    HORIZONTAL_BARS: (HorizontalBarsDrawer, None),
}


class ModuleDrawer(EEnum):
    Square = SQUARE
    Rounded = ROUNDED
    Circle = CIRCLE
    Gapped = GAPPED
    VerticalBars = VERTICAL_BARS
    HorizontalBars = HORIZONTAL_BARS

    @classmethod
    def value_of(
        cls,
        value: str,
        default: Optional["ModuleDrawer"] = None,
        raise_error: bool = True,
    ) -> Optional["ModuleDrawer"]:
        value = value.upper()
        return super().value_of(value, default, raise_error)

    def get_module_drawer(self, is_svg: bool = False) -> Optional[Type[QRModuleDrawer]]:
        if is_svg:
            idx = 1
        else:
            idx = 0
        tmp = _value_map.get(self.value, None)
        if tmp is None:
            return None
        module_drawer_class = tmp[idx]
        if module_drawer_class is None:
            return None
        return module_drawer_class
