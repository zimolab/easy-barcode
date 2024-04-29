from PyQt6.QtWidgets import QApplication
from function2widgets import Color
from qrcode.constants import (
    ERROR_CORRECT_L,
    ERROR_CORRECT_M,
    ERROR_CORRECT_Q,
    ERROR_CORRECT_H,
)
from qrcode.image.styles.moduledrawers import (
    SquareModuleDrawer,
    CircleModuleDrawer,
    GappedSquareModuleDrawer,
)
from qrcode.image.styles.moduledrawers.svg import (
    SvgPathSquareDrawer,
    SvgPathCircleDrawer,
)

from .module_drawer import ModuleDrawer
from .color_mask import ColorMask

FUNC_NAME = QApplication.tr("二维码生成器")
FUNC_DESC = QApplication.tr("")

ITEMS_ERROR_CORRECTION = {
    "L": ERROR_CORRECT_L,
    "M": ERROR_CORRECT_M,
    "Q": ERROR_CORRECT_Q,
    "H": ERROR_CORRECT_H,
}


SQUARE_DRAWER = QApplication.tr("方格")
CIRCLE_DRAWER = QApplication.tr("圆点")
ROUNDED_DRAWER = QApplication.tr("圆角方格")
GAPPED_DRAWER = QApplication.tr("小方格")
VERTICAL_BARS_DRAWER = QApplication.tr("竖线")
HORIZONTAL_BARS_DRAWER = QApplication.tr("横线")
ITEMS_MODULE_DRAWER = {
    SQUARE_DRAWER: ModuleDrawer.Square.value,
    CIRCLE_DRAWER: ModuleDrawer.Circle.value,
    ROUNDED_DRAWER: ModuleDrawer.Rounded.value,
    GAPPED_DRAWER: ModuleDrawer.Gapped.value,
    VERTICAL_BARS_DRAWER: ModuleDrawer.VerticalBars.value,
    HORIZONTAL_BARS_DRAWER: ModuleDrawer.HorizontalBars.value,
}

MODULE_DRAWERS_SUPPORT_SIZE_RATIO = (
    SquareModuleDrawer,
    SvgPathSquareDrawer,
    CircleModuleDrawer,
    SvgPathCircleDrawer,
    GappedSquareModuleDrawer,
)


COLOR_MASK_SOLID_FILL = QApplication.tr("纯色填充")
COLOR_MASK_RADIAL_GRADIENT = QApplication.tr("径向渐变(圆形)")
COLOR_MASK_SQUARE_RADIAL_GRADIENT = QApplication.tr("径向渐变(方形)")
COLOR_MASK_HORIZONTAL_GRADIENT = QApplication.tr("水平渐变")
COLOR_MASK_VERTICAL_GRADIENT = QApplication.tr("垂直渐变")

RADIAL_GRADIENT_LABEL = QApplication.tr("径向渐变")
BACK_COLOR_LABEL = QApplication.tr("背景颜色(全部)")
FRONT_COLOR_LABEL = QApplication.tr("前景颜色({})".format(COLOR_MASK_SOLID_FILL))
CENTER_COLOR_LABEL = QApplication.tr("中心颜色({})".format(RADIAL_GRADIENT_LABEL))
EDGE_COLOR_LABEL = QApplication.tr("边缘颜色({})".format(RADIAL_GRADIENT_LABEL))
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
    COLOR_MASK_SOLID_FILL: ColorMask.SolidFill.value,
    COLOR_MASK_RADIAL_GRADIENT: ColorMask.RadialGradient.value,
    COLOR_MASK_SQUARE_RADIAL_GRADIENT: ColorMask.SquareRadialGradient.value,
    COLOR_MASK_HORIZONTAL_GRADIENT: ColorMask.HorizontalGradient.value,
    COLOR_MASK_VERTICAL_GRADIENT: ColorMask.VerticalGradient.value,
}

COLOR_MASK_REQUIRED_COLOR_LABELS = {
    ColorMask.SolidFill: (
        BACK_COLOR_LABEL,
        FRONT_COLOR_LABEL,
    ),
    ColorMask.RadialGradient: (
        BACK_COLOR_LABEL,
        CENTER_COLOR_LABEL,
        EDGE_COLOR_LABEL,
    ),
    ColorMask.SquareRadialGradient: (
        BACK_COLOR_LABEL,
        CENTER_COLOR_LABEL,
        EDGE_COLOR_LABEL,
    ),
    ColorMask.HorizontalGradient: (
        BACK_COLOR_LABEL,
        LEFT_COLOR_LABEL,
        RIGHT_COLOR_LABEL,
    ),
    ColorMask.VerticalGradient: (
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
# LABEL_FILL_COLOR = QApplication.tr("前景色（填充色）")
# LABEL_BACK_COLOR = QApplication.tr("背景色")
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
DESCRIPTION_OPTIMIZE = QApplication.tr("优化级别")
DESCRIPTION_BOX_SIZE = QApplication.tr(
    "点块尺寸，即指定每个二维码每个点块在最终图像上的像素大小，即每个点块渲染成多少个像素"
)
DESCRIPTION_BORDER = QApplication.tr(
    "边框宽度，即二维码四周的空白边框宽度，合适的边框宽度有助于扫描设备更容易识别二维码"
)
# DESCRIPTION_FILL_COLOR = QApplication.tr("填充颜色，默认为黑色")
# DESCRIPTION_BACK_COLOR = QApplication.tr("背景颜色，默认为白色")
DESCRIPTION_MODULE_DRAWER = QApplication.tr("控制生成二维码内点块元素的形状")
DESCRIPTION_SIZE_RATIO = QApplication.tr(
    "该参数仅在手动指定元素形状后生效，且仅对特定几种形状（Square、GappedSquare、Circle）有效"
)
DESCRIPTION_BACKGROUND_IMAGE_PATH = QApplication.tr(
    "背景图片，若指定了该参数，则<b>颜色遮罩参数</b>不会生效"
)
DESCRIPTION_COLOR_MASK = QApplication.tr(
    "遮罩颜色，不同的遮罩模式所需颜色不同，仅在启用颜色遮罩模式时生效，当选择了背景图片时，该参数不生效"
)
DESCRIPTION_COLOR_MASK_COLORS = QApplication.tr("此参数仅在启用颜色遮罩时生效")
DESCRIPTION_EMBEDED_IMAGE_PATH = QApplication.tr(
    "内嵌图片（logo）路径（当输出文件为svg格式，嵌入图片可能无法生效）"
)

DEFAULT_VALUE_DESCRIPTION_VERSION = QApplication.tr("使用默认值")
DEFAULT_VALUE_DESCRIPTION_ERROR_CORRECTION = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_OPTIMIZE = QApplication.tr("使用默认配置")
DEFAULT_VALUE_DESCRIPTION_BOX_SIZE = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_BORDER = QApplication.tr("")
# DEFAULT_VALUE_DESCRIPTION_FILL_COLOR = QApplication.tr("")
# DEFAULT_VALUE_DESCRIPTION_BACK_COLOR = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_MODULE_DRAWER = QApplication.tr("使用默认配置")
DEFAULT_VALUE_DESCRIPTION_SIZE_RATIO = QApplication.tr("使用默认值（{}）")
DEFAULT_VALUE_DESCRIPTION_BACKGROUND_IMAGE_PATH = QApplication.tr("不使用背景图片")
DEFAULT_VALUE_DESCRIPTION_COLOR_MASK = QApplication.tr("不使用颜色遮罩")
DEFAULT_VALUE_DESCRIPTION_COLOR_MASK_COLORS = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_EMBEDED_IMAGE_PATH = QApplication.tr("不嵌入图片")
DEFAULT_VALUE_DESCRIPTION_VERBOSE = QApplication.tr("")

DEFAULT_VALUE_VERSION = None
DEFAULT_VALUE_ERROR_CORRECTION = "M"
DEFAULT_VALUE_OPTIMIZE = None
DEFAULT_VALUE_BOX_SIZE = 8
DEFAULT_VALUE_BORDER = 2
# DEFAULT_VALUE_FILL_COLOR = Color.from_string("black")
# DEFAULT_VALUE_BACK_COLOR = Color.from_string("white")
DEFAULT_VALUE_MODULE_DRAWER = None
DEFAULT_VALUE_SIZE_RATIO = 1.0
DEFAULT_VALUE_BACKGROUND_IMAGE_PATH = None
DEFAULT_VALUE_COLOR_MASK = COLOR_MASK_SOLID_FILL
DEFAULT_VALUE_COLOR_MASK_COLORS = DEFAULT_COLOR_MASK_COLORS
DEFAULT_VALUE_EMBEDED_IMAGE_PATH = None

ERR_MSG_UNSUPPORTED_FILE_EXTENSION = QApplication.tr("不支持的输出文件格式：{}")
ERR_MSG_UNSUPPORTED_MODULE_DRAWER = QApplication.tr("不支持的点块形状：{}")
ERR_MSG_UNSUPPORTED_SVG_MODULE_DRAWER = QApplication.tr("该点块形状不适用于SVG格式：{}")
ERR_MSG_EMPTY_EMBEDED_IMAGE_PATH = QApplication.tr("嵌入图片路径不能为空")
ERR_MSG_EMBEDED_IMAGE_NOT_FOUND = QApplication.tr("嵌入图片路径不存在")
ERR_MSG_EMPTY_BACKGROUND_IMAGE_PATH = QApplication.tr("背景图片路径不能为空")
ERR_MSG_BACKGROUND_IMAGE_NOT_FOUND = QApplication.tr("背景图片路径不存在")
ERR_MSG_UNKNOWN_COLOR_MASK = QApplication.tr("未知的颜色遮罩类型：{}")
ERR_MSG_INVALID_ERROR_CORRECTION = QApplication.tr("错误的纠错级别：{}")

MSG_COLOR_MASK_IGNORED = QApplication.tr(
    "颜色遮罩与背景图片同时启用时，颜色遮罩参数将不生效"
)
# ERR_MSG_COLOR_MASK_COLORS_NOT_PROVIDED = QApplication.tr(
#     "颜色遮罩已启用，但未提供遮罩颜色！"
# )
