from enum import Enum
from typing import List
from pydantic import BaseModel,dataclasses
from pandas.core.frame import  DataFrame
from . import errors

from abc import ABCMeta
class TypeNameEnum(str,Enum):
    data_frame="data frame"
    series="series"
    object="object"

@dataclasses
class DataFramePort(DataFrame,BaseModel):
    port_type:TypeNameEnum
    optional:bool

    @classmethod
    def get_validators(cls):
        yield cls.validate

    @classmethod
    def validate(cls, values) -> DataFrame:
        print(values)
        if cls.port_type is  None:
            raise errors.NoneIsNotAllowedError()
        return values




