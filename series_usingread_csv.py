import numpy as np
import pandas as pd

#pd.read_csv("file_name")==>gives dataframe .we have to convert to series
#to convert in series==>pd.read_csv("file_name").squeeze("columns")

#with one col
subs=pd.read_csv("subs.csv").squeeze("columns")
   
print(subs)

#with 2 columns
score=pd.read_csv("kohli_ipl.csv",index_col="match_no").squeeze("columns")
print(score)

movie=pd.read_csv("bollywood.csv",index_col="movie").squeeze("columns")
print(movie)
