import pandas as pd

csv1 = pd.read_csv("C:\\Users\\madha\\Desktop\\PandasLibrary\\Students.csv")

print(csv1)

# get the rows
csv1 = pd.read_csv("C:\\Users\\madha\\Desktop\\PandasLibrary\\Students.csv",nrows=4)
print(csv1)

#Get the Column
csv1 = pd.read_csv("C:\\Users\\madha\\Desktop\\PandasLibrary\\Students.csv",usecols=['name'])
print(csv1)

#Get the multiple columns
csv1 = pd.read_csv("C:\\Users\\madha\\Desktop\\PandasLibrary\\Students.csv",usecols=['name','age'])
print(csv1)

# You can also pass the column number instead of column name 
csv1 = pd.read_csv("C:\\Users\\madha\\Desktop\\PandasLibrary\\Students.csv",usecols=[0,1])
print(csv1)

#Skip the rows
csv2 = pd.read_csv("C:\\Users\\madha\\Desktop\\PandasLibrary\\Students.csv",skiprows=[5,10])
print(csv2)

#IndexCol : Give any of the column name data to the index
csv1 = pd.read_csv("C:\\Users\\madha\\Desktop\\PandasLibrary\\Students.csv",index_col=['name'])
print(csv1)

#Change the header by giving any row number
csv1 = pd.read_csv("C:\\Users\\madha\\Desktop\\PandasLibrary\\Students.csv",header=[7])
print(csv1)

#Give the heading using names
csv1 = pd.read_csv("C:\\Users\\madha\\Desktop\\PandasLibrary\\Students.csv",names =['col1','col2','col3','col4'])
print(csv1)

# We can remove heading also by using header = None
csv1 = pd.read_csv("C:\\Users\\madha\\Desktop\\PandasLibrary\\Students.csv", header = None)
print(csv1)

# We can change data type also by specifying column in the form of dictionary
csv1 = pd.read_csv("C:\\Users\\madha\\Desktop\\PandasLibrary\\Students.csv", dtype={"marks":'float'})
print(csv1)