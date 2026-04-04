import pandas as pd
var1 = pd.DataFrame({"A":[1,2,3,4], "B":[11,12,13,14]})
print(var1)
var2= pd.DataFrame({"A":[1,2,3,5], "C":[21,22,23,24]})
print(var2)

#-----------------MERGE()------------------------

# While merging two dataframes, one part(e.g. id) must be common in two dataframes

print(pd.merge(var1,var2, on="A"))

# how ="inner" is by default
# prints all from left + matching from right
print(pd.merge(var1,var2,how ="left"))

# prints all from right + matching from left
print(pd.merge(var1,var2,how="right"))

# Takes ALL rows from both DataFrames and fill missing values with NaN
print(pd.merge(var1,var2,how="outer"))

# shows showing whether each row/column came from left, right, or both DataFrames
print(pd.merge(var1,var2,how="outer",indicator=True))

# join DataFrames based on their row index
print(pd.merge(var1,var2,left_index=True,right_index=True))

#Change the header name
print(pd.merge(var1,var2,left_index=True,right_index=True,suffixes=("name","id")))


#-------------CONCAT()---------------
#simply stack or join data (no matching keys required)
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([11,12,13,14,15])

print(pd.concat([s1,s2]))

d1 = pd.DataFrame({"A":[1,2,3,4], "B":[11,12,13,14]})
d2= pd.DataFrame({"A":[1,2,3,4],  "B":[21,22,23,24]})

print(pd.concat([d1,d2]))

# Print column-wise
print(pd.concat([d1,d2], axis =1))

# outer join Keeps ALL columns from all DataFrames and gives NaN in missing values
d3 = pd.DataFrame({"A":[1,2,3,4], "B":[11,12,13,14]})
d4= pd.DataFrame({"A":[1,2],  "B":[23,24]})
print(pd.concat([d3,d4], axis =1,join="outer"))

# inner join returns common values only
print(pd.concat([d1,d2], axis =1,join="inner"))

# adds a label to each DataFrame so you know the source of data after concatenation
print(pd.concat([d1,d2], axis=1,keys=['d1','d2']))


