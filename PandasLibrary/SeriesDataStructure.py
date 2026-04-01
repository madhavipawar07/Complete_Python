import pandas as pd
x = [1,4,7,2,4,7]
var = pd.Series(x)
print(var)
print(type(var))

#get the element
print(var[2])

#Changing the index
var = pd.Series(x, index = ['a','b','s','n','e','w'])
print(var)

#changing the data type
var = pd.Series(x, dtype= float)
print(var)

#Naming the data
var = pd.Series(x, name ="python")
print(var)

dict = {"name":["Python", "C", "C++", "Java"],"pro":[12,13,14,15],"rank":[1,2,3,4,5]}
var = pd.Series(dict)
print(var)


s = pd.Series(12, index = [1,2,3,4,5])
print(s)

#In numpy library if we'll perform this type of addition then it will throw broadcast address. But pandas return NaN(not a Number) to those values and perform the addition of other values 
s1 = pd.Series(12, index = [1,2,3,4,5])
s2 = pd.Series(12, index = [1,2,3])
print(s1+s2)

