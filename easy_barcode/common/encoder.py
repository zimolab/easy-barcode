import abc
import os.path

from pyguiadapter.interact import ulogging, uprint, upopup

from ._constants import *
from .overwrite_behavior import OverwriteBehavior


class OverwriteNotAllowed(Exception):
    pass


class BaseEncoder(object):

    def __init__(
        self,
        verbose: bool = False,
        enable_timestamp: bool = False,
        timestamp_pattern: str = None,
    ):
        self._verbose = verbose
        self._enable_timestamp = enable_timestamp
        self._timestamp_pattern = timestamp_pattern

    def _check_overwrite_behavior(
        self, behavior: OverwriteBehavior, preview_only: bool, dest_filepath: str
    ):
        if preview_only:
            return
        if not os.path.isfile(dest_filepath):
            return

        if behavior == OverwriteBehavior.NotOverwrite:
            self.error(ERR_MSG_OVERWRITE_NOT_ALLOWED)
            raise OverwriteNotAllowed(ERR_MSG_OVERWRITE_NOT_ALLOWED)
        elif behavior == OverwriteBehavior.Ask:
            if self.show_info_popup(MSG_ASK_OVERWRITE):
                self.warning(MS_OVERWRITE_ALLOWED)
                return
            else:
                self.error(ERR_MSG_OVERWRITE_NOT_ALLOWED)
                raise OverwriteNotAllowed(ERR_MSG_OVERWRITE_NOT_ALLOWED)
        else:
            self.warning(MS_OVERWRITE_ALLOWED)

    @abc.abstractmethod
    def encode(
        self,
        code: str,
        preview_only: bool,
        dest_path: str,
        target_filename: str,
        overwrite_behavior: str,
        verbose: bool,
        **kwargs,
    ):
        self._verbose = verbose is True

        if not isinstance(code, str):
            raise TypeError(f"code must be a string, but got {type(code)}")

        if code.strip() == "":
            self.error(ERR_MSG_EMPTY_CODE)
            raise ValueError(ERR_MSG_EMPTY_CODE)

        if not isinstance(dest_path, str):
            raise TypeError(f"dest_path must be a string, but got {type(dest_path)}")

        if dest_path.strip() == "":
            dest_path = DEFAULT_VALUE_DEST_PATH

        if not os.path.isdir(dest_path):
            self.warning(MSG_CREATE_DEST_PATH)
            os.makedirs(dest_path, exist_ok=True)

        if not isinstance(target_filename, str):
            raise TypeError(
                f"target_filename must be a string, but got {type(target_filename)}"
            )

        if not isinstance(overwrite_behavior, str):
            raise TypeError(
                f"overwrite_behavior must be a string, but got {type(overwrite_behavior)}"
            )
        overwrite_behavior = OverwriteBehavior.value_of(
            overwrite_behavior, default=OverwriteBehavior.Ask
        )

        dest_filepath = os.path.join(dest_path, target_filename)
        base_dir = os.path.dirname(dest_filepath)
        if not os.path.isdir(base_dir):
            os.makedirs(base_dir, exist_ok=True)

        self._check_overwrite_behavior(
            overwrite_behavior,
            preview_only,
            dest_filepath,
        )

    def debug(self, message: str):
        if self._verbose:
            ulogging.debug(
                message,
                timestamp=self._enable_timestamp,
                timestamp_pattern=self._timestamp_pattern,
            )

    def info(self, message: str):
        if self._verbose:
            ulogging.info(
                message,
                timestamp=self._enable_timestamp,
                timestamp_pattern=self._timestamp_pattern,
            )

    def warning(self, message: str):
        if self._verbose:
            ulogging.warning(
                message,
                timestamp=self._enable_timestamp,
                timestamp_pattern=self._timestamp_pattern,
            )

    def error(self, message: str):
        if self._verbose:
            ulogging.critical(
                message,
                timestamp=self._enable_timestamp,
                timestamp_pattern=self._timestamp_pattern,
            )

    @staticmethod
    def show_info_popup(message: str, title: str = POPUP_TITLE_INFO):
        upopup.information(message, title)

    @staticmethod
    def show_warning_popup(message: str, title: str = POPUP_TITLE_WARNING):
        upopup.warning(message, title)

    @staticmethod
    def show_error_popup(message: str, title: str = POPUP_TITLE_ERROR):
        upopup.critical(message, title)

    @staticmethod
    def show_question_popup(message: str, title: str = POPUP_TITLE_ERROR) -> bool:
        return upopup.question(message, title)

    @staticmethod
    def print(message: str = "", html: bool = False):
        uprint.uprint(message, html=html)

    @staticmethod
    def print_image(image_path: str):
        uprint.uprint_image(image_path)
