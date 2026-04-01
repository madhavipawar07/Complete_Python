import pandas as pd

csv_1 = pd.read_csv("C:\\Users\\madha\\Desktop\\PandasLibrary\\Students.csv")

print(csv_1)

# Get the index information
print(csv_1.index) #stop is always n+1 value

# Give the total column names
print(csv_1.columns)

# Gives all mathematical values(count, mean, max, std) values of numerical values present in the data
print(csv_1.describe())

# Get the fix amount of upper data rather than complete data
print(csv_1.head(4)) # It will show the first 4 rows data

# Gives the fix amount of lower data 
print(csv_1.tail(2)) #It will show last two rows data

# Gives the specific range of data
print(csv_1[:4])#gives the values based on index
print(csv_1[6:9])
print(type(csv_1))

# Show the index in the array format
print(csv_1.index.array)

# Convert the index in numpy array
print(csv_1.to_numpy())

# Sort index in descending order
print(csv_1.sort_index(axis=0,ascending=False))# axis = 0 means rows and axis = 1 means columns

# Change the column data by specifying row number
#csv_1['name'][11] ="Jagruti" # NOt a proper way
# Use this one
csv_1.loc[11,"name"] = "Jagruti" # 11 number row index will update the name as Jagruti

# Get a specific data using loc
print(csv_1.loc[[2,5],['name','marks']])
print(csv_1.loc[:, ['name', 'marks']])


#Get a particular data value using iloc
print(csv_1.iloc[0,2]) #0 specifies the row index number and 2 specifies column number

#Drop a specific column/row
print(csv_1.drop("marks",axis =1 ))
print(csv_1.drop(6,axis = 0))
