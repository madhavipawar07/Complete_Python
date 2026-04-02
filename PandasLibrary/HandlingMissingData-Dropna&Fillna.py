import pandas as pd 

var = pd.read_csv("C:\\Users\\madha\\Desktop\\PythonSeries\\PandasLibrary\\Students.csv")

print(var)

# dropna() will drop the rows where missing values are present
print(var.dropna())

# You can drop a column also where missing values are present
print(var.dropna(axis=1))

# If data contains a row which is completely null then you can use 'how' parameter 
print(var.dropna(how="any")) #It means it will remove all the rows which are completely null and the rows which contains some of the null values

print(var.dropna(how="all"))# It will remove the only rows which contains complete null data, but it will keep rows where some of the null values are present

#remove the null values from specified column
print(var.dropna(subset="age"))

# This will remove all null values and put some values in place of them and returns the data
# var.dropna(inplace=True)
# print(var)

# This remove single null values
print(var.dropna(thresh=4))

# fillna is used to fill the missing values 
print(var.fillna("Python"))

# Fil particular data in particular column using dictionary
print(var.fillna({"marks":"Python","age":"java"}))


# If you want to fill data based on the previous value , use method = ffill/bfill
#print(var.fillna(method="ffill"))
#print(var.fillna(method="ffill",axis=0))

# inplace 
#print(var.fillna(12,inplace=True))# It will display 12 value in place of all missing values

# It will check the limit, it is 1 so it will place the python value in the first missing place of each column
print(var.fillna("Python",limit=1)) 
print(var.fillna("Python",limit=3))# Now it will print python value in first 3 missing places of  each column

