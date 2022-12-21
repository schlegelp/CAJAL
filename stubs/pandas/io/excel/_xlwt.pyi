from pandas._typing import FilePath as FilePath, StorageOptions as StorageOptions, WriteExcelBuffer as WriteExcelBuffer
from pandas.io.excel._base import ExcelWriter as ExcelWriter
from pandas.io.excel._util import combine_kwargs as combine_kwargs, validate_freeze_panes as validate_freeze_panes
from typing import Any
from xlwt import Workbook as Workbook, XFStyle as XFStyle

class XlwtWriter(ExcelWriter):
    def __init__(self, path: Union[FilePath, WriteExcelBuffer, ExcelWriter], engine: Union[str, None] = ..., date_format: Union[str, None] = ..., datetime_format: Union[str, None] = ..., encoding: Union[str, None] = ..., mode: str = ..., storage_options: StorageOptions = ..., if_sheet_exists: Union[str, None] = ..., engine_kwargs: Union[dict[str, Any], None] = ..., **kwargs) -> None: ...
    @property
    def book(self) -> Workbook: ...
    @book.setter
    def book(self, other: Workbook) -> None: ...
    @property
    def sheets(self) -> dict[str, Any]: ...
    @property
    def fm_date(self): ...
    @property
    def fm_datetime(self): ...
