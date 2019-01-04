# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time: 2018/10/09 17:18
# @author: gerry, modified by Siyuan

import pandas as pd
from genpro.PublicUtils import check_error
from genpro.PublicUtils.check_error import GenError


# global parameters
indices = [0]
start = None
end = None
names = None
mode = 'indices'

def main_row_selection(data, bool_array):
    return genpro_row_selection(data=data, mode=mode, indices=indices, start=start, end=end, names=names, bool_array = bool_array)


def genpro_row_selection(data, mode = 'indices', indices=0, start=None, end=None, names = None,  bool_array = None):
    """
    Select rows of input data

    :param data: DataFrame, input data
    :param indices: list of int, indices of rows
    :param start: int, start index, if indices is not given, then start must be given
    :param end: int, end index(exclusive), if indices is not given, then end must be given
    :return: data_selected, DataFrame
    """
    check_error.check_df_type(data, -1)
    check_error.check_data_empty(data, -2)
    if mode not in ['indices', 'range','names']:
        raise GenError(-380)

    if bool_array is not None:
        check_error.check_data_type(bool_array, pd.Series, -324)
        if bool_array.dtype != bool:
            raise GenError(-326)
        if len(bool_array) != data.shape[0]:
            raise GenError(-327)
        data_selected = data.iloc[bool_array.values]

    else:
        if mode == 'indices':
            check_error.check_data_type(indices, list, -3)
            for i in indices:
                check_error.check_integer(i, -4)
                if i >= data.shape[0]:
                    raise GenError(-9)
            if len(indices) == 1:
                indices = indices[0]
            data_selected = data.iloc[indices]

        elif mode == 'range':
            check_error.check_integer(start, -5)
            check_error.check_integer(end, -6)
            data_selected = data.iloc[start:end]

        elif mode == 'names':
            check_error.check_data_type(names, list, -381)
            data.index = list(map(str, data.index))
            for i in names:
                if i not in data.index:
                    raise GenError(-379)
            data_selected = data.loc[names]
    if isinstance(data_selected, pd.Series):
        data_selected = data_selected.to_frame().T
    
    return  data_selected