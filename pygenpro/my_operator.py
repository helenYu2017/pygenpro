from pydantic import validator,ValidationError
from pygenpro.types import DFPort,BasicOperator,df_port
from pygenpro.validators import check_df_same_size
import pandas as pd
from pandas import Series, DataFrame
import numpy as np


data1 = DataFrame(np.arange(15).reshape(3,5),index=['one','two','three'],columns=['a','b','c','d','e'])
data2 = DataFrame(np.arange(12).reshape(3,4),index=['one','two','three'],columns=['a','b','c','d'])
data3 =DataFrame(np.arange(15).reshape(3,5),index=['one','two','three'],columns=['a','b','c','d','e'])


class Add(BasicOperator):
    data1:df_port()
    data2:df_port(optional=True)

    @validator("data2")
    def same_size(cls,v,values,**kwargs):
        v1 = values['data1']
        v2 = v
        check_df_same_size(v1,v2)
        return values

    @classmethod
    def result(cls):
        result = data1.values + data2.values
        return  pd.DataFrame(result)

result=None


try:
    result=Add(data1=data1,data2=data2)
except ValidationError as e:
    print(str(e))

