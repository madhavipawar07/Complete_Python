import pandas as pd
var = pd.DataFrame({"a":[1,2,3,4],"b":[5,6,7,8]})
print(var)
#Addition
var["c"] = var["a"]+var["b"]
print(var)

#Subtraction
var["c"] = var["a"] - var["b"]
print(var)

#Multiplication
var["c"] = var["a"] * var["b"]
print(var)

#Division
var["c"] = var["a"] / var["b"]
print(var)