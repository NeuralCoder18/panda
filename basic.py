import numpy as np
import pandas as pd
#what is panda
#Pandas is a fast,powerful,flexible and easy to use open source data analysis and manipulation tool,built on top of the Python proramming language
#Pandas Series 
#A Pandas Series is like a column in a table.It is a 1-D array holding data of any type
#Series consist of index (automatically. generated)and values
#=====================================================================================================================================================================
# making series using python lists
country=['India','Pakistan','USA','Nepal','Srilanka']
print(pd.Series(country))
#Not always but generally Panda calls string as object

# Custom Index
marks=[67,57,89,100]
subjects=['maths','english','science','hindi']
print(pd.Series(marks,index=subjects))

#Setting a name
print(pd.Series(marks,index=subjects,name='Rudra ke marks'))

#------------------------------
#making series using dictionary
#------------------------------
#key become index and values become values
marks={
    'maths':67,
    'english':57,
    'science':89,
    'hindi':100
}
marks_series=pd.Series(marks)
print(marks_series)