from pydantic import BaseModel,validator,dataclasses
from pygenpro import errors
from pygenpro.types import DataFramePort,TypeNameEnum

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

data = DataFrame(np.arange(15).reshape(3,5),index=['one','two','three'],columns=['a','b','c','d','e'])
print(data)

@dataclasses
class Add(BaseModel):
    data1:DataFramePort(port_type=TypeNameEnum.data_frame,optional=True)
    data2:DataFramePort(port_type=TypeNameEnum.data_frame,optional=True)

    @validator('data2')
    def size_match(cls, v, values, **kwargs):
        if 'data1' in values and len(v) != len(values['data1']):
            raise errors.SizeNotEqual('the size of data1 is not equal to data2')
        return v

