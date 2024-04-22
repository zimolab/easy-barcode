from function2widgets import CheckBox
from function2widgets import CheckBoxArgs
from function2widgets import ColorEdit
from function2widgets import ColorEditArgs
from function2widgets import ComboBox, ComboBoxArgs
from function2widgets import DictEditor, DictEditorArgs
from function2widgets import FilePathEdit, FilePathEditArgs
from function2widgets import FloatSpinBox, FloatSpinBoxArgs
from function2widgets import IntSpinBox, IntSpinBoxArgs
from function2widgets import LineEdit
from function2widgets import LineEditArgs

from easy_barcode.common.configs import UNIVERSAL_CONFIGS
from ._constants import *

BARCODE_ENCODE_CONFIGS = {
    **UNIVERSAL_CONFIGS,
    "barcode_type": {
        "widget_class": ComboBox.__name__,
        "widget_args": ComboBoxArgs(
            parameter_name="AS-IS",
            label=LABEL_BARCODE_TYPE,
            description=DESCRIPTION_BARCODE_TYPE,
            default=DEFAULT_VALUE_BARCODE_TYPE,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_BARCODE_TYPE,
            items=BARCODE_TYPES,
        ),
    },
    "text": {
        "widget_class": LineEdit.__name__,
        "widget_args": LineEditArgs(
            parameter_name="AS-IS",
            label=LABEL_TEXT,
            description=DESCRIPTION_TEXT,
            default=DEFAULT_VALUE_TEXT,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_TEXT,
        ),
    },
    "extra_args": {
        "widget_class": DictEditor.__name__,
        "widget_args": DictEditorArgs(
            parameter_name="AS-IS",
            label=LABEL_EXTRA_ARGS,
            default=DEFAULT_VALUE_EXTRA_ARGS,
            description=DESCRIPTION_EXTRA_ARGS,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_EXTRA_ARGS,
            button_text=BUTTON_EXTRA_ARGS,
            window_title=WINDOW_TITLE_EXTRA_ARGS,
            display_current_value=False,
        ),
    },
    "dpi": {
        "widget_class": IntSpinBox.__name__,
        "widget_args": IntSpinBoxArgs(
            parameter_name="AS-IS",
            label=LABEL_DPI,
            description=DESCRIPTION_DPI,
            default=DEFAULT_VALUE_DPI,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_DPI,
            min_value=150,
            max_value=2000,
            step=50,
        ),
    },
    "compress": {
        "widget_class": CheckBox.__name__,
        "widget_args": CheckBoxArgs(
            parameter_name="AS-IS",
            label=LABEL_COMPRESS,
            description=DESCRIPTION_COMPRESS,
            default=DEFAULT_VALUE_COMPRESS,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_COMPRESS,
            text=CHECKBOX_COMPRESS,
        ),
    },
    "module_width": {
        "widget_class": FloatSpinBox.__name__,
        "widget_args": FloatSpinBoxArgs(
            parameter_name="AS-IS",
            label=LABEL_MODULE_WIDTH,
            description=DESCRIPTION_MODULE_WIDTH,
            default=DEFAULT_VALUE_MODULE_WIDTH,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_MODULE_WIDTH,
            min_value=0.1,
            max_value=10.0,
            step=0.1,
            decimals=1,
        ),
    },
    "module_height": {
        "widget_class": FloatSpinBox.__name__,
        "widget_args": FloatSpinBoxArgs(
            parameter_name="AS-IS",
            label=LABEL_MODULE_HEIGHT,
            description=DESCRIPTION_MODULE_HEIGHT,
            default=DEFAULT_VALUE_MODULE_HEIGHT,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_MODULE_HEIGHT,
            min_value=10.0,
            max_value=100.0,
            step=0.5,
            decimals=2,
        ),
    },
    "quiet_zone": {
        "widget_class": FloatSpinBox.__name__,
        "widget_args": FloatSpinBoxArgs(
            parameter_name="AS-IS",
            label=LABEL_QUIET_ZONE,
            description=DESCRIPTION_QUIET_ZONE,
            default=DEFAULT_VALUE_QUIET_ZONE,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_QUIET_ZONE,
            min_value=0.1,
            max_value=100.0,
            step=0.1,
            decimals=2,
        ),
    },
    "font_path": {
        "widget_class": FilePathEdit.__name__,
        "widget_args": FilePathEditArgs(
            parameter_name="AS-IS",
            label=LABEL_FONT_PATH,
            description=DESCRIPTION_FONT_PATH,
            default=DEFAULT_VALUE_FONT_PATH,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_FONT_PATH,
            button_text=BUTTON_FONT_PATH,
            dialog_title=DIALOG_TITLE_FONT_PATH,
            filters=FILTERS_FONT_FILE,
        ),
    },
    "font_size": {
        "widget_class": IntSpinBox.__name__,
        "widget_args": IntSpinBoxArgs(
            parameter_name="AS-IS",
            label=LABEL_FONT_SIZE,
            description=DESCRIPTION_FONT_SIZE,
            default=DEFAULT_VALUE_FONT_SIZE,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_FONT_SIZE,
            min_value=1,
            max_value=100,
        ),
    },
    "text_distance": {
        "widget_class": FloatSpinBox.__name__,
        "widget_args": FloatSpinBoxArgs(
            parameter_name="AS-IS",
            label=LABEL_TEXT_DISTANCE,
            description=DESCRIPTION_TEXT_DISTANCE,
            default=DEFAULT_VALUE_TEXT_DISTANCE,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_TEXT_DISTANCE,
            min_value=1.0,
            max_value=100.0,
            step=0.1,
            decimals=2,
        ),
    },
    "background": {
        "widget_class": ColorEdit.__name__,
        "widget_args": ColorEditArgs(
            parameter_name="AS-IS",
            label=LABEL_BACKGROUND,
            description=DESCRIPTION_BACKGROUND,
            default=DEFAULT_VALUE_BACKGROUND,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_BACKGROUND,
            with_alpha=False,
        ),
    },
    "foreground": {
        "widget_class": ColorEdit.__name__,
        "widget_args": ColorEditArgs(
            parameter_name="AS-IS",
            label=LABEL_FOREGROUND,
            description=DESCRIPTION_FOREGROUND,
            default=DEFAULT_VALUE_FOREGROUND,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_FOREGROUND,
            with_alpha=False,
        ),
    },
    "center_text": {
        "widget_class": CheckBox.__name__,
        "widget_args": CheckBoxArgs(
            parameter_name="AS-IS",
            label=LABEL_CENTER_TEXT,
            description=DESCRIPTION_CENTER_TEXT,
            default=DEFAULT_VALUE_CENTER_TEXT,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_CENTER_TEXT,
            text=CHECKBOX_CENTER_TEXT,
        ),
    },
}
