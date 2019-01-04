from decimal import Decimal
from pathlib import Path
from typing import Union
from pydantic import PydanticTypeError,PydanticValueError

class GenTypeError(PydanticTypeError):
    code="GenTypeError"

class GenValueError(PydanticValueError):
    code="GenValueError"

class NoneIsNotAllowedError(GenTypeError):
    code = 'none.not_allowed'
    msg_template = 'none is not an allow value'

class IntegerError(GenTypeError):
    msg_template = 'value is not a valid integer'

class SizeNotEqual(GenValueError):
    code = 'size.not_equal'
    msg_template = 'size must be equal'

class DFTypeError(GenTypeError):
    msg_template = 'value is not a valid DataFrame'

class SeriesTypeError(GenTypeError):
    msg_template = 'value is not a valid Series'