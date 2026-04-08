import pandas as pd

var = pd.DataFrame({"days":[1,2,3,4,5,6],"eng":[11,12,15,19,10,18],"maths":[17,18,13,19,15,14]})

print(var)

print(pd.melt(var))