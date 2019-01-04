
from . import errors
import pandas as pd
from pydantic.utils import change_exception
def not_none_validator(v):
    if v is None:
        raise errors.NoneIsNotAllowedError()
    return v

def check_df_same_size(v1,v2)->bool:
    if v1.shape[0] != v2.shape[0] and v1.shape[0] != 1 and v2.shape[0] != 1:
        raise errors.SizeNotEqual()
    if v1.shape[1] != v2.shape[1] and v1.shape[1] != 1 and v2.shape[1] != 1:
        raise errors.SizeNotEqual()
    return True

#type validator
def float_validator(v) -> float:
    if isinstance(v, float):
        return v
    with change_exception(errors.FloatTypeError, TypeError, ValueError):
        return float(v)

def df_validator(v)->pd.core.frame.DataFrame:
    if  isinstance(v, pd.core.frame.DataFrame):
        return v
    with change_exception(errors.DFTypeError, TypeError, ValueError):
        return pd.DataFrame(v)

def series_validator(v)->pd.core.frame.Series:
    if  isinstance(v, pd.core.frame.Series):
        return v
    with change_exception(errors.SeriesTypeError, TypeError, ValueError):
        return pd.Series(v)
