from pandas.core.frame import DataFrame,Series
from pygenpro.types import BasicOperator,DFPort,SeriesPort,series_port,multi_type
from pydantic import ValidationError
from pydantic.types import PositiveInt
from typing import Union,NewType,Tuple,List
import numpy as np
from enum import Enum

class ModeEnum(Enum):
    names="names"
    indices="indices"
    range="range"

# Indices=NewType("indices",List[int])
# Names=NewType("names",List[str])
# Start=NewType("start",PositiveInt)
# End=NewType("end",PositiveInt)
# Range=NewType("range",Tuple[Start,End])


class SelectRow(BasicOperator):
    data:DFPort
    bool_array:series_port(optional=False)
    mode:ModeEnum



if __name__=="__main__":
    data = DataFrame(np.arange(15).reshape(3, 5), index=['one', 'two', 'three'], columns=['a', 'b', 'c', 'd', 'e'])
    bool_array=Series([True,False,True,False])
    try:
        SelectRow(data=data,bool_array=bool_array,mode="indices",config=(9,9))
    except ValidationError as e:
        print(str(e))
