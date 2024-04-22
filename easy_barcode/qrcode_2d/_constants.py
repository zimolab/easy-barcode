from PyQt6.QtWidgets import QApplication
from function2widgets import Color
from qrcode.constants import (
    ERROR_CORRECT_L,
    ERROR_CORRECT_M,
    ERROR_CORRECT_Q,
    ERROR_CORRECT_H,
)
from qrcode.image.styles.colormasks import (
    SolidFillColorMask,
    RadialGradiantColorMask,
    SquareGradiantColorMask,
    HorizontalGradiantColorMask,
    VerticalGradiantColorMask,
)
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

FUNC_NAME = QApplication.tr("二维码生成器")
FUNC_DESC = QApplication.tr("")

ITEMS_ERROR_CORRECTION = {
    "L": ERROR_CORRECT_L,
    "M": ERROR_CORRECT_M,
    "Q": ERROR_CORRECT_Q,
    "H": ERROR_CORRECT_H,
}


SQUARE_DRAWER = QApplication.tr("Square")
CIRCLE_DRAWER = QApplication.tr("Circle")
ROUNDED_DRAWER = QApplication.tr("Rounded")
GAPPED_DRAWER = QApplication.tr("Gapped")
VERTICAL_BARS_DRAWER = QApplication.tr("Vertical Bars")
HORIZONTAL_BARS_DRAWER = QApplication.tr("Horizontal Bars")

ITEMS_MODULE_DRAWER = {
    SQUARE_DRAWER: (SquareModuleDrawer, SvgPathSquareDrawer),
    CIRCLE_DRAWER: (CircleModuleDrawer, SvgPathCircleDrawer),
    ROUNDED_DRAWER: RoundedModuleDrawer,
    GAPPED_DRAWER: GappedSquareModuleDrawer,
    VERTICAL_BARS_DRAWER: VerticalBarsDrawer,
    HORIZONTAL_BARS_DRAWER: HorizontalBarsDrawer,
}
PNG_DRAWER_IDX = 0
SVG_DRAWER_IDX = 1

COLOR_MASK_SOLID_FILL = QApplication.tr("纯色填充")
COLOR_MASK_RADIAL_GRADIENT = QApplication.tr("径向渐变(圆形)")
COLOR_MASK_SQUARE_RADIAL_GRADIENT = QApplication.tr("径向渐变(方形)")
COLOR_MASK_HORIZONTAL_GRADIENT = QApplication.tr("水平渐变")
COLOR_MASK_VERTICAL_GRADIENT = QApplication.tr("垂直渐变")
_RADIAL_GRADIENT = QApplication.tr("径向渐变")
BACK_COLOR_LABEL = QApplication.tr("背景颜色(全部)")
FRONT_COLOR_LABEL = QApplication.tr("前景颜色({})".format(COLOR_MASK_SOLID_FILL))
CENTER_COLOR_LABEL = QApplication.tr("中心颜色({})".format(_RADIAL_GRADIENT))
EDGE_COLOR_LABEL = QApplication.tr("边缘颜色({})".format(_RADIAL_GRADIENT))
LEFT_COLOR_LABEL = QApplication.tr(
    "左侧颜色({})".format(COLOR_MASK_HORIZONTAL_GRADIENT)
)
RIGHT_COLOR_LABEL = QApplication.tr(
    "右侧颜色({})".format(COLOR_MASK_HORIZONTAL_GRADIENT)
)
TOP_COLOR_LABEL = QApplication.tr("上侧颜色({})".format(COLOR_MASK_VERTICAL_GRADIENT))
BOTTOM_COLOR_LABEL = QApplication.tr(
    "下侧颜色({})".format(COLOR_MASK_VERTICAL_GRADIENT)
)

DEFAULT_COLOR_MASK_COLORS = {
    BACK_COLOR_LABEL: Color(255, 255, 255),
    FRONT_COLOR_LABEL: Color(0, 0, 0),
    CENTER_COLOR_LABEL: Color(0, 0, 0),
    EDGE_COLOR_LABEL: Color(0, 0, 255),
    LEFT_COLOR_LABEL: Color(0, 0, 0),
    RIGHT_COLOR_LABEL: Color(0, 0, 255),
    TOP_COLOR_LABEL: Color(0, 0, 0),
    BOTTOM_COLOR_LABEL: Color(0, 0, 255),
}

ITEMS_COLOR_MASK = {
    COLOR_MASK_SOLID_FILL: SolidFillColorMask,
    COLOR_MASK_RADIAL_GRADIENT: RadialGradiantColorMask,
    COLOR_MASK_SQUARE_RADIAL_GRADIENT: SquareGradiantColorMask,
    COLOR_MASK_HORIZONTAL_GRADIENT: HorizontalGradiantColorMask,
    COLOR_MASK_VERTICAL_GRADIENT: VerticalGradiantColorMask,
}
COLOR_MASK_REQUIRED_COLOR_LABELS = {
    SolidFillColorMask: (
        BACK_COLOR_LABEL,
        FRONT_COLOR_LABEL,
    ),
    RadialGradiantColorMask: (
        BACK_COLOR_LABEL,
        CENTER_COLOR_LABEL,
        EDGE_COLOR_LABEL,
    ),
    SquareGradiantColorMask: (
        BACK_COLOR_LABEL,
        CENTER_COLOR_LABEL,
        EDGE_COLOR_LABEL,
    ),
    HorizontalGradiantColorMask: (
        BACK_COLOR_LABEL,
        LEFT_COLOR_LABEL,
        RIGHT_COLOR_LABEL,
    ),
    VerticalGradiantColorMask: (
        BACK_COLOR_LABEL,
        TOP_COLOR_LABEL,
        BOTTOM_COLOR_LABEL,
    ),
}

FILTERS_EMBEDED_IMAGE_PATH = QApplication.tr(
    "PNG文件(*.png);;JPG文件(*.jpg);;JPEG文件(*.jpeg);;GIF文件(*.gif);;所有文件(*.*)"
)

BUTTON_EMBEDED_IMAGE_PATH = QApplication.tr("选择")

LABEL_VERSION = QApplication.tr("二维码版本")
LABEL_ERROR_CORRECTION = QApplication.tr("纠错级别")
LABEL_OPTIMIZE = QApplication.tr("优化级别")
LABEL_BOX_SIZE = QApplication.tr("点块大小")
LABEL_BORDER = QApplication.tr("边框宽度")
LABEL_FILL_COLOR = QApplication.tr("前景色（填充色）")
LABEL_BACK_COLOR = QApplication.tr("背景色")
LABEL_MODULE_DRAWER = QApplication.tr("点块形状")
LABEL_SIZE_RATIO = QApplication.tr("尺寸比例")
LABEL_BACKGROUND_IMAGE_PATH = QApplication.tr("背景图片路径")
LABEL_COLOR_MASK = QApplication.tr("颜色遮罩")
LABEL_COLOR_MASK_COLORS = QApplication.tr("颜色遮罩参数")
LABEL_EMBEDED_IMAGE_PATH = QApplication.tr("嵌入图片")

DESCRIPTION_VERSION = QApplication.tr(
    "该参数控制生成二维码的尺寸，从1到40，使用默认配置时，在生成图片时自动判断"
)
DESCRIPTION_ERROR_CORRECTION = QApplication.tr(
    "纠错级别，级别越高，纠错能力越强，但载荷容量越小"
)
DESCRIPTION_OPTIMIZE = QApplication.tr("")
DESCRIPTION_BOX_SIZE = QApplication.tr("")
DESCRIPTION_BORDER = QApplication.tr("")
DESCRIPTION_FILL_COLOR = QApplication.tr("")
DESCRIPTION_BACK_COLOR = QApplication.tr("")
DESCRIPTION_MODULE_DRAWER = QApplication.tr("")
DESCRIPTION_SIZE_RATIO = QApplication.tr("")
DESCRIPTION_BACKGROUND_IMAGE_PATH = QApplication.tr("")
DESCRIPTION_COLOR_MASK = QApplication.tr("")
DESCRIPTION_COLOR_MASK_COLORS = QApplication.tr("")
DESCRIPTION_EMBEDED_IMAGE_PATH = QApplication.tr("")

DEFAULT_VALUE_DESCRIPTION_VERSION = QApplication.tr("使用默认值")
DEFAULT_VALUE_DESCRIPTION_ERROR_CORRECTION = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_OPTIMIZE = QApplication.tr("使用默认配置")
DEFAULT_VALUE_DESCRIPTION_BOX_SIZE = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_BORDER = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_FILL_COLOR = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_BACK_COLOR = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_MODULE_DRAWER = QApplication.tr("使用默认配置")
DEFAULT_VALUE_DESCRIPTION_SIZE_RATIO = QApplication.tr("使用默认值（{}）")
DEFAULT_VALUE_DESCRIPTION_BACKGROUND_IMAGE_PATH = QApplication.tr("不使用背景图片")
DEFAULT_VALUE_DESCRIPTION_COLOR_MASK = QApplication.tr("不使用颜色遮罩")
DEFAULT_VALUE_DESCRIPTION_COLOR_MASK_COLORS = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_EMBEDED_IMAGE_PATH = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_VERBOSE = QApplication.tr("")

DEFAULT_VALUE_VERSION = None
DEFAULT_VALUE_ERROR_CORRECTION = "M"
DEFAULT_VALUE_OPTIMIZE = None
DEFAULT_VALUE_BOX_SIZE = None
DEFAULT_VALUE_BORDER = None
DEFAULT_VALUE_FILL_COLOR = Color.from_string("black")
DEFAULT_VALUE_BACK_COLOR = Color.from_string("white")
DEFAULT_VALUE_MODULE_DRAWER = None
DEFAULT_VALUE_SIZE_RATIO = 1.0
DEFAULT_VALUE_BACKGROUND_IMAGE_PATH = None
DEFAULT_VALUE_COLOR_MASK = None
DEFAULT_VALUE_COLOR_MASK_COLORS = None
DEFAULT_VALUE_EMBEDED_IMAGE_PATH = None
