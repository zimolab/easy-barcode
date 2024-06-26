import os.path

from PyQt6.QtWidgets import QApplication

from .overwrite_behavior import OverwriteBehavior

ITEM_OVERWRITE_ASK = QApplication.tr("询问")
ITEM_OVERWRITE_NOT_OVERWRITE = QApplication.tr("不覆盖")
ITEM_OVERWRITE_OVERWRITE = QApplication.tr("覆盖")
ITEMS_OVERWRITE_BEHAVIOR = {
    ITEM_OVERWRITE_ASK: str(OverwriteBehavior.Ask),
    ITEM_OVERWRITE_OVERWRITE: str(OverwriteBehavior.Overwrite),
    ITEM_OVERWRITE_NOT_OVERWRITE: str(OverwriteBehavior.NotOverwrite),
}

POPUP_TITLE_INFO = QApplication.tr("提示")
POPUP_TITLE_ERROR = QApplication.tr("错误")
POPUP_TITLE_WARNING = QApplication.tr("警告")
POPUP_TITLE_QUESTION = QApplication.tr("选择")

ERR_MSG_EMPTY_CODE = QApplication.tr("待编码数据为空！")
ERR_MSG_OVERWRITE_NOT_ALLOWED = QApplication.tr("目标文件已存在，不允许覆盖该文件！")
ERR_MSG_EMPTY_DEST_FILEPATH = QApplication.tr("目标文件路径为空！")
MSG_CREATE_DEST_PATH = QApplication.tr("目标路径不存在，将自动创建该路径！")
MSG_ASK_OVERWRITE = QApplication.tr("目标文件已存在，是否允许覆盖该文件？")
MS_OVERWRITE_ALLOWED = QApplication.tr("目标文件将被覆盖！")

CHECKBOX_VERBOSE = QApplication.tr("启用详细模式")

BUTTON_DEST_PATH = QApplication.tr("选择")

PLACEHOLDER_CODE = QApplication.tr("请输入待编码的文本")

LABEL_CODE = QApplication.tr("待编码数据")
LABEL_DEST_PATH = QApplication.tr("目标路径")
LABEL_TARGET_FILENAME = QApplication.tr("目标文件名")
LABEL_OVERWRITE_BEHAVIOR = QApplication.tr("覆盖行为")
LABEL_VERBOSE = QApplication.tr("打印详细信息")

DESCRIPTION_CODE = QApplication.tr(
    "待编码数据的长度需符合相应限制条件，否则可能造成编码失败"
)
DESCRIPTION_DEST_PATH = QApplication.tr("")
DESCRIPTION_TARGET_FILENAME = QApplication.tr("")
DESCRIPTION_OVERWRITE_BEHAVIOR = QApplication.tr("文件已存在时的处理方式")
DESCRIPTION_VERBOSE = QApplication.tr("")

DEFAULT_VALUE_DESCRIPTION_CODE = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_DEST_PATH = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_TARGET_FILENAME = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_OVERWRITE_BEHAVIOR = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_VERBOSE = QApplication.tr("")
DEFAULT_VALUE_DESCRIPTION_KWARGS = QApplication.tr("")

DEFAULT_VALUE_CODE = ""
DEFAULT_VALUE_DEST_PATH = os.path.normcase(os.path.abspath("./"))
DEFAULT_VALUE_TARGET_FILENAME = ""
DEFAULT_VALUE_OVERWRITE_BEHAVIOR = ITEM_OVERWRITE_ASK
DEFAULT_VALUE_VERBOSE = True

PREVIEW_ONLY_FORMAT = ".png"
