# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time: 2018/06/27 15:18
# @author: qian yang

import pandas as pd
from pydantic import validator,ValidationError
from pygenpro.types import df_port,BasicOperator
from pygenpro.validators import check_df_same_size
from pandas.core.frame import Series, DataFrame
import numpy as np


class Add(BasicOperator):
    data1:df_port()
    data2:df_port(optional=True)

    @validator("data2")
    def same_size(cls, v, values, **kwargs):
        v1 = values['data1']
        v2 = v
        check_df_same_size(v1, v2)
        return values

    @classmethod
    def result(cls)->DataFrame:
        return genpro_add(data1, data2)


def genpro_add(data1, data2):

    """
    Add the input data1 and data2

    :param data1: DataFrame, input data
    :param data2: DataFrame, input data
    :return: added data, DataFrame
    """
    result = data1.values + data2.values
    return  pd.DataFrame(result)


if __name__=="__main__":
    data1 = DataFrame(np.arange(15).reshape(3,5),index=['one','two','three'],columns=['a','b','c','d','e'])
    data2 = DataFrame(np.arange(12).reshape(3,4),index=['one','two','three'],columns=['a','b','c','d'])
    data3 =DataFrame(np.arange(15).reshape(3,5),index=['one','two','three'],columns=['a','b','c','d','e'])
    try:
        result=Add(data1=data1,data2=data2)
    except ValidationError as e:
        print(str(e))


