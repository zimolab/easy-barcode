import base64
import tempfile
import os.path

from typing import Any, Union

from pyguiadapter.interact import ulogging, uprint, upopup

from ._constants import *
from .overwrite_behavior import OverwriteBehavior


class OverwriteNotAllowed(Exception):
    pass


class BaseEncoder(object):

    def __init__(
        self,
        verbose: bool = False,
        enable_timestamp: bool = True,
        timestamp_pattern: str = None,
    ):
        self._verbose = verbose
        self._enable_timestamp = enable_timestamp
        self._timestamp_pattern = timestamp_pattern

    def _check_overwrite_behavior(
        self,
        behavior: OverwriteBehavior,
        preview_only: bool,
        dest_path: str,
        target_filename: str,
    ):

        if preview_only:
            return

        if not target_filename:
            self.error(ERR_MSG_EMPTY_DEST_FILEPATH)
            raise ValueError(ERR_MSG_EMPTY_DEST_FILEPATH)

        dest_filepath = os.path.join(dest_path, target_filename)
        base_dir = os.path.dirname(dest_filepath)
        if not os.path.isdir(base_dir):
            os.makedirs(base_dir, exist_ok=True)

        if not os.path.isfile(dest_filepath):
            return

        print(type(behavior))

        if behavior == OverwriteBehavior.NotOverwrite:
            self.error(ERR_MSG_OVERWRITE_NOT_ALLOWED)
            raise OverwriteNotAllowed(ERR_MSG_OVERWRITE_NOT_ALLOWED)
        elif behavior == OverwriteBehavior.Ask:
            if self.show_question_popup(MSG_ASK_OVERWRITE):
                self.warning(MS_OVERWRITE_ALLOWED)
                return
            else:
                self.error(ERR_MSG_OVERWRITE_NOT_ALLOWED)
                raise OverwriteNotAllowed(ERR_MSG_OVERWRITE_NOT_ALLOWED)
        else:
            self.warning(MS_OVERWRITE_ALLOWED)

    # noinspection PyUnusedLocal
    def encode(
        self,
        *,
        code: str = None,
        preview_only: bool = None,
        dest_path: str = None,
        target_filename: str = None,
        overwrite_behavior: str = None,
        verbose: bool = None,
        **kwargs,
    ):
        self._verbose = verbose is True

        if not isinstance(code, str):
            raise TypeError(f"code must be a string, but got {type(code)}")

        if not code:
            self.error(ERR_MSG_EMPTY_CODE)
            raise ValueError(ERR_MSG_EMPTY_CODE)

        if not isinstance(dest_path, str):
            raise TypeError(f"dest_path must be a string, but got {type(dest_path)}")

        dest_path = self._get_dest_path(dest_path)

        if not os.path.isdir(dest_path):
            self.warning(MSG_CREATE_DEST_PATH)
            os.makedirs(dest_path, exist_ok=True)

        if not isinstance(target_filename, str):
            raise TypeError(
                f"target_filename must be a string, but got {type(target_filename)}"
            )

        if preview_only and target_filename:
            self.warning(MSG_FILE_WILL_NOT_CREATED)

        if not isinstance(overwrite_behavior, str):
            raise TypeError(
                f"overwrite_behavior must be a string, but got {type(overwrite_behavior)}"
            )

        overwrite_behavior = self._get_overwrite_behavior(overwrite_behavior)

        self._check_overwrite_behavior(
            overwrite_behavior, preview_only, dest_path, target_filename
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

    def print_result(self, result: Any, preview_only: bool):
        if preview_only:
            result.seek(0)
            image_data = result.read()
            self.print_image_data(image_data, PREVIEW_ONLY_FORMAT)
        else:
            self.print_image(result)

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

    @staticmethod
    def print_image_data(data: bytes, image_type: str):
        encoded_data = base64.b64encode(data).decode("utf-8")
        data_url = f"data:image/{image_type};base64,{encoded_data}"
        uprint.uprint("\n")
        uprint.uprint(f"<img src='{data_url}' />", html=True)
        uprint.uprint("\n")

    @staticmethod
    def open_target_file(target_filepath: str, preview_only: bool):
        if not preview_only:
            return open(target_filepath, "wb")

        tmp_file = tempfile.NamedTemporaryFile(
            mode="wb+",
            delete_on_close=True,
            suffix=PREVIEW_ONLY_FORMAT,
        )
        return tmp_file

    @staticmethod
    def add_options_to(options: dict, **kvs):
        for k, v in kvs.items():
            if v is not None:
                options[k] = v

    @staticmethod
    def _get_dest_path(path: str) -> str:
        path = path.strip()
        if not path:
            return DEFAULT_VALUE_DEST_PATH
        return path

    @staticmethod
    def _get_overwrite_behavior(
        behavior: Union[str, OverwriteBehavior, None]
    ) -> OverwriteBehavior:
        default_behavior = ITEMS_OVERWRITE_BEHAVIOR.get(
            DEFAULT_VALUE_OVERWRITE_BEHAVIOR
        )
        default_behavior = OverwriteBehavior.value_of(default_behavior)

        if behavior is None:
            return default_behavior

        if isinstance(behavior, OverwriteBehavior):
            return behavior

        tmp = ITEMS_OVERWRITE_BEHAVIOR.get(behavior, None)
        if tmp is not None:
            return OverwriteBehavior.value_of(tmp)

        return OverwriteBehavior.value_of(behavior.upper(), default=default_behavior)
