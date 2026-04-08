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

print(var.pivot(index="days",columns="st_name"))