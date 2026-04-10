import pandas as pd

var = pd.DataFrame({"days":[1,2,3,4,5,6],"eng":[11,12,15,19,10,18],"maths":[17,18,13,19,15,14]})

print(var)

#------------------------MELT()------------------
#it is used for reshaping data — specifically converting data from wide format → long format

print(pd.melt(var))

print(pd.melt(var,id_vars=["days"]))


print(pd.melt(var,id_vars=["days"],var_name="python"))

#---------------------PIVOT()----------------
# It is used to reshape data from long format → wide format

var = pd.DataFrame({"days":[1,2,3,4,5,6],"st_name":['a','b','c','a','b','c',],"eng":[11,12,15,19,10,18],"maths":[17,18,13,19,15,14]})

print(var)

# At least two arguements passing is must otherwise it will throw error
print(var.pivot(index="days",columns="st_name"))

# Get particular column data only
print(var.pivot(index="days",columns="st_name",values="eng"))

# Performing aggregate functions
#  pivot() does not support aggfunc. It only works when data has unique combinations. We have to use pivot_table() instead

var = pd.DataFrame({"days":[1,1,1,1,2,2],"st_name":['a','b','c','a','b','c',],"eng":[11,12,15,19,10,18],"maths":[17,18,13,19,15,14]})

print(var.pivot_table(index="st_name",columns="days",aggfunc="mean"))

print(var.pivot_table(index="st_name",columns="days",aggfunc="sum"))

#margins=True is used to add overall summary totals (row-wise and column-wise) in a pivot table
print(var.pivot_table(index="st_name",columns="days",aggfunc="mean",margins=True))

#margins=True is used to add overall summary totals (row-wise and column-wise) in a pivot table
print(var.pivot_table(index="st_name",columns="days",aggfunc="mean",margins=True))