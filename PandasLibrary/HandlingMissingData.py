import pandas as pd
csv1 = pd.read_csv("C:\\Users\\madha\\Desktop\\PandasLibrary\\Students.csv")
print(csv1)

#-------------REPLACE FUNCTION---------

# Replace the 20 as 21 
var = csv1.replace(to_replace=20,value=21)
print(var)

# Replace the name with specifued name
var =csv1.replace(to_replace="Harshada",value="Rakesh")
print(var)

# Replace this list of numbers as 22
var =csv1.replace([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],22)
print(var)

# It will check capital letters in all data and replace them with specified name
var =csv1.replace("[A-Z]","Python",regex=True)
print(var)

# You can achieve it using dictionary format also
var =csv1.replace({"name": '[A-Z]'},22,regex=True)
print(var)

#Forward Filling
# var = csv1.replace(8, method ='ffill')
# print(var)

#Backward Filling using limit
# var = csv1.replace(1,method = 'bfill',limit =2 )
# print(var)

# If you want to change the data in original dataset then use inplace..it will directly change in original data rather than making its copy
# var = csv1.replace(1, method = "ffill",limit = 2,inplace=True)
# print(var)

#-----------INTERPOLATE FUNCTION----------

#interpolate() function is used to fill the null values...It analyzes the previous values and on that basis generates the values and automatically fill them in null values. It works only on numerical values not strings
var = pd.read_csv("C:\\Users\\madha\\Desktop\\PandasLibrary\\Students.csv")
print(var)

print(var.interpolate())

#Method list of interpolate
# method : {"linear","time","index","values","nearest","zero","slinear","quadratic","cubic","barycentric","krogh","polynomial","spline","piecewise-polynomial","from_derivatives","pchip","akima"}
#By default it is always linear
 
print(var.interpolate(method ='linear',axis=0))

# It will fil 2 NaN values
print(var.interpolate(limit =2))

# Limit Directions = Forward, backward, both
print(var.interpolate(limit_direction="forward",limit =2))

# limit_area = inside : It means limit the area..if the selected option is outside then limit will not work
print(var.interpolate(limit_area="inside",limit=2))

# inplace: same working as mentioned in replace function
print(var.interpolate(limit_direction="both",limit=2,inplace=False))