import pandas as pd

x = pd.DataFrame({"A":[1,2,3,4,5],"B":[0,6,7,8,9]})

x.insert(2,"python",x["A"]) #2 represents the index where you want column, 'Python' is a name of column

print(x)


x.insert(1,"python_1",[11,12,13,14,15])
print(x)

x['python_12'] = x['A'] [:3]
print(x)

# Delete Operation
var = pd.DataFrame({'A':[1,2,3,4,5], 'B':[9,8,7,6,5], 'C':[11,12,13,14,15]})
print(var)

var1 =var.pop("A")
print(var1)

del var["C"]
print(var)