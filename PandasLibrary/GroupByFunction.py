import pandas as pd
var= pd.DataFrame({"A":["a","a","b","c","a","c","a","b"], "S1":[11,12,13,25,21,12,13,12], "S2":[11,15,23,21,11,24,23,23]})

print(var)

#print the same data in a group 
var1= var.groupby("A")
print(var1)
# To see the grouped data use for loop
for x,y in var1:
    print(x)
    print(y)
 
 # Print the data of single group
print(var1.get_group("a"))
print(var1.get_group("c"))

# get minimum data among all
print(var1.min())

# get maximum
print(var1.max())

# get mean
print(var1.mean())

# you can convert the data of dataframe into list also and perform various list operations on it 
li = list(var1)
print(li)