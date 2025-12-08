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


#size==>give size of series 
print(marks_series.size)

#dtype==>give data type of series
print(marks_series.dtype)

#name==>give name of series
print(marks_series.name)

#is_unique==>tells whether all elements of my series is unique or not
print(marks_series.is_unique)

#index==>gives index of the series
print(marks_series.index)

#values==>gives all values of series
print(marks_series.values)