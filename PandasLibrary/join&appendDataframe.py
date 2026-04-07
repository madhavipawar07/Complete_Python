import pandas as pd
var1 = pd.DataFrame({"A":[1,2,3,4], "B":[11,12,13,14]})

var2= pd.DataFrame({"C":[10,20,30,40],"D":[21,22,23,24]})

#-------------JOIN()----------------------

print(var1.join(var2))

# If any value is missing from data then it will print NaN in missing palce
var1 = pd.DataFrame({"A":[1,2,3,4], "B":[11,12,13,14]})

var2= pd.DataFrame({"C":[10,20],"D":[21,22]})

print(var1.join(var2))

# changing the index
var1 = pd.DataFrame({"A":[1,2,3,4], "B":[11,12,13,14]},index=['a','b','c','d'])

var2= pd.DataFrame({"C":[10,20],"D":[21,22]},index=['a','b'])

print(var1.join(var2))

# Performing join operations

print(var1.join(var2,how="inner"))

print(var1.join(var2,how="left"))

print(var1.join(var2,how="right"))

print(var1.join(var2,how="outer"))

#sometimes both DataFrames have same column names This creates a conflict...To solve this, we use: lsuffix & rsuffix 
var1 = pd.DataFrame({"A":[1,2,3,4], "B":[11,12,13,14]},index=['a','b','c','d'])

var2= pd.DataFrame({"B":[10,20],"D":[21,22]},index=['a','b'])

print(var1.join(var2,how="outer",lsuffix="-1",rsuffix='-2'))


# --------------------APPEND()-------------------------

# append() adds one DataFrame below another,  works row-wise (vertical stacking) and is mainly used to add new records, although it is now deprecated and replaced by concat(). On the other hand, join() combines DataFrames column-wise (horizontal merging) based on their index, adding columns from one DataFrame to another. 

var1 = pd.DataFrame({"A":[1,2,3,4], "B":[11,12,13,14]},index=['a','b','c','d'])

var2= pd.DataFrame({"B":[10,20],"D":[21,22]},index=['a','b'])

# This will throw error because earlier versions of Pandas had DataFrame.append().Now it is deprecated and completely removed So  latest Pandas version does not support it
print(var1.append(var2))


