from function2widgets import (
    ColorEdit,
    IntSpinBox,
    IntSpinBoxArgs,
    FloatSpinBox,
    FloatSpinBoxArgs,
)
from function2widgets import ColorEditArgs
from function2widgets import ComboBox, ComboBoxArgs
from function2widgets import FilePathEdit, FilePathEditArgs
from function2widgets import Slider, SliderArgs
from pyguiadapter import get_param_widget_factory

from easy_barcode.common.configs import UNIVERSAL_CONFIGS
from ._constants import *
from .widget import ColorsGroupWidget, ColorsGroupWidgetArgs

_param_widget_factory = get_param_widget_factory()
if not _param_widget_factory.is_registered(ColorsGroupWidget.__name__):
    _param_widget_factory.register(ColorsGroupWidget.__name__, ColorsGroupWidget)

QRCODE_ENCODE_CONFIGS = {
    **UNIVERSAL_CONFIGS,
    "version": {
        "widget_class": Slider.__name__,
        "widget_args": SliderArgs(
            parameter_name="AS-IS",
            label=LABEL_VERSION,
            description=DESCRIPTION_VERSION,
            default=DEFAULT_VALUE_VERSION,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_VERSION,
            min_value=1,
            max_value=40,
            step=1,
            tracking=True,
            tick_interval=2,
            tick_position="Above",
            show_value_label=True,
        ),
    },
    "error_correction": {
        "widget_class": ComboBox.__name__,
        "widget_args": ComboBoxArgs(
            parameter_name="AS-IS",
            label=LABEL_ERROR_CORRECTION,
            description=DESCRIPTION_ERROR_CORRECTION,
            default=DEFAULT_VALUE_ERROR_CORRECTION,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_ERROR_CORRECTION,
            items=list(ITEMS_ERROR_CORRECTION.keys()),
        ),
    },
    "optimize": {
        "widget_class": Slider.__name__,
        "widget_args": SliderArgs(
            parameter_name="AS-IS",
            label=LABEL_OPTIMIZE,
            description=DESCRIPTION_OPTIMIZE,
            default=DEFAULT_VALUE_OPTIMIZE,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_OPTIMIZE,
            min_value=0,
            max_value=100,
            step=1,
            tracking=True,
            tick_interval=5,
            tick_position="Above",
            show_value_label=True,
        ),
    },
    "box_size": {
        "widget_class": IntSpinBox.__name__,
        "widget_args": IntSpinBoxArgs(
            parameter_name="AS-IS",
            label=LABEL_BOX_SIZE,
            description=DESCRIPTION_BOX_SIZE,
            default=DEFAULT_VALUE_BOX_SIZE,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_BOX_SIZE,
            min_value=1,
            max_value=9999,
            step=1,
        ),
    },
    "border": {
        "widget_class": IntSpinBox.__name__,
        "widget_args": IntSpinBoxArgs(
            parameter_name="AS-IS",
            label=LABEL_BORDER,
            description=DESCRIPTION_BORDER,
            default=DEFAULT_VALUE_BORDER,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_BORDER,
            min_value=1,
            max_value=100,
            step=1,
        ),
    },
    # "fill_color": {
    #     "widget_class": ColorEdit.__name__,
    #     "widget_args": ColorEditArgs(
    #         parameter_name="AS-IS",
    #         label=LABEL_FILL_COLOR,
    #         description=DESCRIPTION_FILL_COLOR,
    #         default=DEFAULT_VALUE_FILL_COLOR,
    #         default_value_description=DEFAULT_VALUE_DESCRIPTION_FILL_COLOR,
    #         with_alpha=False,
    #     ),
    # },
    # "back_color": {
    #     "widget_class": ColorEdit.__name__,
    #     "widget_args": ColorEditArgs(
    #         parameter_name="AS-IS",
    #         label=LABEL_BACK_COLOR,
    #         description=DESCRIPTION_BACK_COLOR,
    #         default=DEFAULT_VALUE_BACK_COLOR,
    #         default_value_description=DEFAULT_VALUE_DESCRIPTION_BACK_COLOR,
    #         with_alpha=False,
    #     ),
    # },
    "module_drawer": {
        "widget_class": ComboBox.__name__,
        "widget_args": ComboBoxArgs(
            parameter_name="AS-IS",
            label=LABEL_MODULE_DRAWER,
            description=DESCRIPTION_MODULE_DRAWER,
            default=DEFAULT_VALUE_MODULE_DRAWER,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_MODULE_DRAWER,
            items=list(ITEMS_MODULE_DRAWER.keys()),
        ),
    },
    "size_ratio": {
        "widget_class": FloatSpinBox.__name__,
        "widget_args": FloatSpinBoxArgs(
            parameter_name="AS-IS",
            label=LABEL_SIZE_RATIO,
            description=DESCRIPTION_SIZE_RATIO,
            default=DEFAULT_VALUE_SIZE_RATIO,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_SIZE_RATIO,
            min_value=0.001,
            max_value=1.00,
            step=0.01,
            decimals=3,
            hide_default_value_widget=False,
        ),
    },
    "background_image_path": {
        "widget_class": FilePathEdit.__name__,
        "widget_args": FilePathEditArgs(
            parameter_name="AS-IS",
            label=LABEL_BACKGROUND_IMAGE_PATH,
            description=DESCRIPTION_BACKGROUND_IMAGE_PATH,
            default=DEFAULT_VALUE_BACKGROUND_IMAGE_PATH,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_BACKGROUND_IMAGE_PATH,
            button_text=BUTTON_EMBEDED_IMAGE_PATH,
            filters=FILTERS_EMBEDED_IMAGE_PATH,
        ),
    },
    "color_mask": {
        "widget_class": ComboBox.__name__,
        "widget_args": ComboBoxArgs(
            parameter_name="AS-IS",
            label=LABEL_COLOR_MASK,
            description=DESCRIPTION_COLOR_MASK,
            default=DEFAULT_VALUE_COLOR_MASK,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_COLOR_MASK,
            items=list(ITEMS_COLOR_MASK.keys()),
        ),
    },
    "color_mask_colors": {
        "widget_class": ColorsGroupWidget.__name__,
        "widget_args": ColorsGroupWidgetArgs(
            parameter_name="AS-IS",
            label=LABEL_COLOR_MASK_COLORS,
            description=DESCRIPTION_COLOR_MASK_COLORS,
            default=DEFAULT_VALUE_COLOR_MASK_COLORS,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_COLOR_MASK_COLORS,
            columns=2,
            colors=DEFAULT_COLOR_MASK_COLORS,
            with_alpha=False,
        ),
    },
    "embeded_image_path": {
        "widget_class": FilePathEdit.__name__,
        "widget_args": FilePathEditArgs(
            parameter_name="AS-IS",
            label=LABEL_EMBEDED_IMAGE_PATH,
            description=DESCRIPTION_EMBEDED_IMAGE_PATH,
            default=DEFAULT_VALUE_EMBEDED_IMAGE_PATH,
            default_value_description=DEFAULT_VALUE_DESCRIPTION_EMBEDED_IMAGE_PATH,
            button_text=BUTTON_EMBEDED_IMAGE_PATH,
            filters=FILTERS_EMBEDED_IMAGE_PATH,
        ),
    },
}
