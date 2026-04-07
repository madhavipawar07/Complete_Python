import pandas as pd
var1 = pd.DataFrame({"A":[1,2,3,4], "B":[11,12,13,14]})

var2= pd.DataFrame({"C":[10,20,30,40],"D":[21,22,23,24]})

print(var1.join(var2))

# If any value is missing from data then it will print NaN in missing palce
var1 = pd.DataFrame({"A":[1,2,3,4], "B":[11,12,13,14]})

var2= pd.DataFrame({"C":[10,20],"D":[21,22]})

print(var1.join(var2))

