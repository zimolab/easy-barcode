from typing import Optional

from easy_barcode.eenum import EEnum


class OverwriteBehavior(EEnum):
    Ask = "ASK"
    NotOverwrite = "NOT_OVERWRITE"
    Overwrite = "OVERWRITE"

    @classmethod
    def value_of(
        cls,
        value: str,
        default: Optional["OverwriteBehavior"] = None,
        raise_error: bool = True,
    ) -> Optional["OverwriteBehavior"]:
        value = value.upper()
        return super().value_of(value, default, raise_error)
