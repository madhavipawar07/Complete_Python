import pandas as pd
#List
l = [1,2,3,4,5]
var = pd.DataFrame(l)
print(var)

#Dictionary 
d = {"name":['a','b','c','d'], "id":[1,2,3,4]}
var1 = pd.DataFrame(d)
print(var1)

#Get a particular data
print(var1["name"][2])

#Accessing a particular column
d1 = {"a":['a','b','c','d'], "s":[1,2,3,4],'e':[5,6,7,8],1:[1,2,3,4]}
var3 = pd.DataFrame(d1,columns=["s",2])
print(var3)

#Changing the index
var3 = pd.DataFrame(d1,index=['a','s','d','f'])
print(var3)

list_1 = [[1,2,3,4,5],[11,12,13,14,15]]
var = pd.DataFrame(list_1)
print(var)

#Using series data structure
sr = {'a':pd.Series([1,2,3,4,5]), 'r':pd.Series([11,12,13,14,15])}
var = pd.DataFrame(sr)
print(var)