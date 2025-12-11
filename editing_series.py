import numpy as np
import pandas as pd
marks={
    'maths':67,
    'english':57,
    'science':89,
    'hindi':100
}
marks_series=pd.Series(marks,name='Rudra ke marks')
print(marks_series)
#using indexing
marks_series[1]=100
print(marks_series)

#what if an index does not exist
marks_series['sst']=90#-->dot show error add an sst row
print(marks_series)#if you only read it will give error
