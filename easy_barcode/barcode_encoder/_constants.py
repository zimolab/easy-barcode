from PyQt6.QtWidgets import QApplication
from function2widgets import Color
from barcode import PROVIDED_BARCODES

FUNC_NAME = QApplication.tr("条形码生成器")
FUNC_DESC = QApplication.tr("")

BARCODE_TYPES = sorted(PROVIDED_BARCODES)


CHECKBOX_COMPRESS = QApplication.tr("生成压缩的SVG")
CHECKBOX_CENTER_TEXT = QApplication.tr("使文字居中")
BUTTON_EXTRA_ARGS = QApplication.tr("查看/编辑")
WINDOW_TITLE_EXTRA_ARGS = QApplication.tr("编辑额外参数")
DIALOG_TITLE_FONT_PATH = QApplication.tr("选择字体文件")
BUTTON_FONT_PATH = QApplication.tr("选择")

FILTERS_FONT_FILE = QApplication.tr(
    "字体文件(*.ttf);;字体文件(*.otf);;字体文件(*.ttc);;字体文件(*.otf);;所有文件(*.*)"
)

MSG_COMPRESS_IGNORED = QApplication.tr("非SVG模式下，压缩SVG选项将被忽略！")
MSG_DPI_IGNORED = QApplication.tr("svg模式下，分辨率参数将被忽略！")


LABEL_TEXT = QApplication.tr("自定义文本")
LABEL_BARCODE_TYPE = QApplication.tr("条码类型")
LABEL_DPI = QApplication.tr("分辨率")
LABEL_COMPRESS = QApplication.tr("压缩SVG")
LABEL_MODULE_WIDTH = QApplication.tr("条块宽度")
LABEL_MODULE_HEIGHT = QApplication.tr("条块高度")
LABEL_QUIET_ZONE = QApplication.tr("左右留白")
LABEL_FONT_PATH = QApplication.tr("字体路径")
LABEL_FONT_SIZE = QApplication.tr("字体大小")
LABEL_TEXT_DISTANCE = QApplication.tr("文字与条码间距")
LABEL_BACKGROUND = QApplication.tr("背景色")
LABEL_FOREGROUND = QApplication.tr("前景色")
LABEL_CENTER_TEXT = QApplication.tr("文字居中")
LABEL_EXTRA_ARGS = QApplication.tr("额外参数")

DESCRIPTION_TEXT = QApplication.tr(
    "自定义文字，若指定该参数，则条码下方的文字将显示为该参数指定的文字"
)
DESCRIPTION_BARCODE_TYPE = QApplication.tr(
    "选择要生成的条码类型，不同的条码支持的数据容量大小及参数均有所区别，具体参见对应条码类型规范"
)
DESCRIPTION_DPI = QApplication.tr("生成图片的分辨率，该参数仅对生成PNG格式图片有效")
DESCRIPTION_COMPRESS = QApplication.tr("是否压缩SVG文件，该参数仅对生成SVG格式图片有效")
DESCRIPTION_MODULE_WIDTH = QApplication.tr("条码中每个条块所占的宽度（单位mm）")
DESCRIPTION_MODULE_HEIGHT = QApplication.tr("条码中每个条块所占的高度（单位mm）")
DESCRIPTION_QUIET_ZONE = QApplication.tr("条码距离左右的边距（单位mm）")
DESCRIPTION_FONT_PATH = QApplication.tr("文字字体路径")
DESCRIPTION_FONT_SIZE = QApplication.tr("文字字体大小（单位pt）")
DESCRIPTION_TEXT_DISTANCE = QApplication.tr("文字与条码距离（单位mm）")
DESCRIPTION_BACKGROUND = QApplication.tr("背景颜色")
DESCRIPTION_FOREGROUND = QApplication.tr("前景（文字）颜色")
DESCRIPTION_CENTER_TEXT = QApplication.tr("文字是否居中")
DESCRIPTION_EXTRA_ARGS = QApplication.tr(
    "输入条码类型对应的额外参数，不同类型的条码可以有不同的参数，比如Code39条码接受add_checksum参数，UPC-A接受make_ean参数等等,"
    "不同条码类型接受的额外的参数及其含义参见：<a href='https://python-barcode.readthedocs.io/en/stable/supported-formats.html'>"
    "python-barcode supported-formats</a>"
)

DEFAULT_VALUE_DESCRIPTION_TEXT = QApplication.tr("无自定义文本")
DEFAULT_VALUE_DESCRIPTION_BARCODE_TYPE = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_DPI = QApplication.tr("使用默认值")
DEFAULT_VALUE_DESCRIPTION_COMPRESS = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_MODULE_WIDTH = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_MODULE_HEIGHT = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_QUIET_ZONE = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_FONT_PATH = QApplication.tr("使用默认字体")
DEFAULT_VALUE_DESCRIPTION_FONT_SIZE = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_TEXT_DISTANCE = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_BACKGROUND = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_FOREGROUND = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_CENTER_TEXT = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_EXTRA_ARGS = QApplication.tr("无额外参数")

DEFAULT_VALUE_TEXT = None
DEFAULT_VALUE_BARCODE_TYPE = "code39"
DEFAULT_VALUE_DPI = None
DEFAULT_VALUE_COMPRESS = True
DEFAULT_VALUE_MODULE_WIDTH = 0.2
DEFAULT_VALUE_MODULE_HEIGHT = 15.0
DEFAULT_VALUE_QUIET_ZONE = 6.5
DEFAULT_VALUE_FONT_PATH = None
DEFAULT_VALUE_FONT_SIZE = 10
DEFAULT_VALUE_TEXT_DISTANCE = 5.0
DEFAULT_VALUE_BACKGROUND = Color.from_string("white")
DEFAULT_VALUE_FOREGROUND = Color.from_string("black")
DEFAULT_VALUE_CENTER_TEXT = True
DEFAULT_VALUE_EXTRA_ARGS = None
