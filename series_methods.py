import numpy as np
import pandas as pd
subs=pd.read_csv("subs.csv").squeeze("columns")
df=pd.read_csv("kohli_ipl.csv",index_col="match_no")
score = df.iloc[:, 0].copy()    # make it independent

movie=pd.read_csv("bollywood.csv",index_col="movie").squeeze("columns")

# head and tail
#head-->by default gives you top 5 rows but you can also modify according to your wish
#tail-->by default gives last 5 rows but you can modify it according to your wish
print(subs.head())
print(subs.head(3))
print(subs.tail())

#sample-->randomly gives you one row from your entire data set but you can modify it
print(movie.sample())
print(movie.sample(5))

#value_counts --> movies==>gives values and their respective frequencies
print(movie.value_counts())

#sort_values-->temporary changes
print(score.sort_values())#-->in ascending order
print(score.sort_values(ascending=False))#-->in descending order
#for top score in entire data
print(score.sort_values(ascending=False).head(1))#-->gives index and values
print(score.sort_values(ascending=False).head(1).values)#-->giver arr[113]
print(score.sort_values(ascending=False).head(1).values[0])#-->gives value

# This changes only the copy (score), NOT the original DataFrame
# we have to write code score.sort_values(inplace=True)
score.sort_values(inplace=True)#(on trying to make change in actual dataframe panda shows error to protect data from being corrupt)
print(score)#to change main dataset df.iloc[:, 0] = df.iloc[:, 0].sort_values().values


# ❓ Does squeeze() change the original dataset?
# ❌ NO — squeeze() NEVER changes the dataset
# subs = pd.read_csv("subs.csv").squeeze("columns")


# What it does:

# Converts DataFrame → Series (if only one column)

# Does NOT modify the CSV

# Does NOT modify DataFrame

# Only changes the object subs in memory

# It is just a shape conversion, not a data change.

#==============================================================================================================
# ❓ Is df.iloc[:,0] = ... really necessary?
# ✅ YES — IF you want the dataset changed.

# Because:

# df.iloc[:, 0]    # is a view (read-only)


# You cannot sort or edit it directly.

# So you MUST reassign:

# df.iloc[:, 0] = df.iloc[:, 0].sort_values().values


# This gives pandas a brand-new updated column and safely replaces the old one.
print(type(df))



#------------------------------------------------------------------------------------------------------------------
#sort_index--->sort index in ascnding or descending order
print(movie.sort_index())
#same inplace concept

#SERIES MATHS METHODS
# count-->dont count missing values
# size --> counts missing values
print(score.count())

#sum &product
print(subs.sum())# product as sum
print(subs.product())

#mean/median/mode/standard deviation/variance
print(subs.mean())
print(score.median())
print(movie.mode())
print(subs.std())
print(score.var())

#min/max
print(subs.max())
print(subs.min())

#describe-->gives summary 
print(score.describe())