from enum import Enum
from typing import Any,List,Type,Tuple,Mapping
from pydantic import BaseModel,dataclasses
from pandas.core.frame import  DataFrame,Series
from . import errors

from .validators import (
    df_validator,
    not_none_validator,
    series_validator,
)

from abc import ABCMeta

__all__ = [
    "PortDataTypeEnum",
    "DFPort",
    "SeriesPort",
    "ModelPort",
    "df_port"
]


class BasicOperator(BaseModel):
    pass


class PortDataTypeEnum(str,Enum):
    data_frame="DataFrame"
    series="Series"
    object="Object"

class PortTypeMeta(type):
    def __new__(cls, name, bases, dct):
        new_cls = type.__new__(cls, name, bases, dct)
        return new_cls


class DFPortTypeMeta(DataFrame,metaclass=PortTypeMeta):
    port_type=PortDataTypeEnum.data_frame
    optional:bool=True

    @classmethod
    def get_validators(cls):
        yield not_none_validator
        yield df_validator
        yield cls.validate

    @classmethod
    def validate(cls, values) -> DataFrame:

        return values


def df_port(*, optional=True) -> Type[DataFrame]:
    # use kwargs then define conf in a dict to aid with IDE type hinting
    namespace = dict(port_type=PortDataTypeEnum.data_frame,optional=optional)
    return type('DFPort', (DFPortTypeMeta,), namespace)


class SeriesPortTypeMeta(Series,metaclass=PortTypeMeta):
    port_type=PortDataTypeEnum.series
    optional:bool=True

    @classmethod
    def get_validators(cls):
        yield not_none_validator
        yield series_validator
        yield cls.validate

    @classmethod
    def validate(cls, values) -> DataFrame:

        return values

def series_port(*, optional=True) -> Type[DataFrame]:
    # use kwargs then define conf in a dict to aid with IDE type hinting
    namespace = dict(port_type=PortDataTypeEnum.series,optional=optional)
    return type('SeriesPort', (SeriesPortTypeMeta,), namespace)

#Model port
class ModelPortTypeMeta(object,metaclass=PortTypeMeta):
    port_type=PortDataTypeEnum.object
    optional:bool=True

    @classmethod
    def get_validators(cls):
        yield not_none_validator
        yield cls.validate

    @classmethod
    def validate(cls, values) -> DataFrame:

        return values


def model_port(*, optional=True) -> Type[DataFrame]:
    # use kwargs then define conf in a dict to aid with IDE type hinting
    namespace = dict(port_type=PortDataTypeEnum.object,optional=optional)
    return type('ModelPort', (ModelPortTypeMeta,), namespace)

DFPort=df_port()
SeriesPort=series_port()
ModelPort=model_port()

#modeType
class GroupTypeMeta(Tuple):
    mode_map:dict

    @classmethod
    def get_validators(cls):
        yield not_none_validator
        yield cls.validate

    @classmethod
    def validate(cls, values) -> Tuple:
        modeValue=values[0]
        attriValue=values[1]
        if cls.mode_map[modeValue] is not None:
            typeStr=cls.mode_map[modeValue]
            if not isinstance(attriValue,typeStr):
                raise TypeError("fffff")
        return values
def multi_type(*, mode_map) -> Type[DataFrame]:
    # use kwargs then define conf in a dict to aid with IDE type hinting
    namespace = dict(mode_map=mode_map)
    return type('MultiType', (GroupTypeMeta,), namespace)