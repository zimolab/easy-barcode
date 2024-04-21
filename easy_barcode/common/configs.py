from function2widgets import CheckBox
from function2widgets import CheckBoxArgs
from function2widgets import LineEdit
from function2widgets import LineEditArgs
from function2widgets import PlainTextEdit, PlainTextEditArgs
from function2widgets import DirPathEdit, DirPathEditArgs
from function2widgets import RadioButtonGroup, RadioButtonGroupArgs


from ._constants import *


UNIVERSAL_CONFIGS = {
    "code": {
        "widget_class": PlainTextEdit.__name__,
        "widget_args": PlainTextEditArgs(
            parameter_name="AS-IS",
            label=LABEL_CODE,
            description=DESCRIPTION_CODE,
            default=DEFAULT_VALUE_CODE,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_CODE,
            placeholder=PLACEHOLDER_CODE,
            line_wrap_mode=True,
        ),
    },
    "preview_only": {
        "widget_class": CheckBox.__name__,
        "widget_args": CheckBoxArgs(
            parameter_name="AS-IS",
            label=LABEL_PREVIEW_ONLY,
            description=DESCRIPTION_PREVIEW_ONLY,
            default=DEFAULT_VALUE_PREVIEW_ONLY,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_PREVIEW_ONLY,
            text=CHECKBOX_PREVIEW_ONLY,
        ),
    },
    "dest_path": {
        "widget_class": DirPathEdit.__name__,
        "widget_args": DirPathEditArgs(
            parameter_name="AS-IS",
            label=LABEL_DEST_PATH,
            description=DESCRIPTION_DEST_PATH,
            default=DEFAULT_VALUE_DEST_PATH,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_DEST_PATH,
            button_text=BUTTON_DEST_PATH,
        ),
    },
    "target_filename": {
        "widget_class": LineEdit.__name__,
        "widget_args": LineEditArgs(
            parameter_name="AS-IS",
            label=LABEL_TARGET_FILENAME,
            description=DESCRIPTION_TARGET_FILENAME,
            default=DEFAULT_VALUE_TARGET_FILENAME,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_TARGET_FILENAME,
            clear_button=True,
        ),
    },
    "overwrite_behavior": {
        "widget_class": RadioButtonGroup.__name__,
        "widget_args": RadioButtonGroupArgs(
            parameter_name="AS-IS",
            label=LABEL_OVERWRITE_BEHAVIOR,
            description=DESCRIPTION_OVERWRITE_BEHAVIOR,
            default=DEFAULT_VALUE_OVERWRITE_BEHAVIOR,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_OVERWRITE_BEHAVIOR,
            items=ITEMS_OVERWRITE_BEHAVIOR,
            column_count=3,
        ),
    },
    "verbose": {
        "widget_class": CheckBox.__name__,
        "widget_args": CheckBoxArgs(
            parameter_name="AS-IS",
            label=LABEL_VERBOSE,
            description=DESCRIPTION_VERBOSE,
            default=DEFAULT_VALUE_VERBOSE,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_VERBOSE,
            text=CHECKBOX_VERBOSE,
        ),
    },
}
