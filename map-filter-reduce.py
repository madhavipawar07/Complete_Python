#******map()******
# 
# # def square(x):
#     return x*x

# l=[1,2,3,4,5,6,8]
# newl = list(map(square,l))
# print(newl)

 #using lambda
l=[1,2,3,4,5,6,8]
newl = list(map(lambda x:x*x,l))
print(newl)

#*******filter()********

l=[1,2,3,4,5,6,8]
newl = list(filter(lambda a: a>2,l))
print(newl)


#*********reduce()********

from functools import reduce

numbers = [1,2,3,4,5,6,]

sum = reduce(lambda m,n: m+n,numbers)
print (sum)

#Using def function
from functools import reduce

def sum(a,b):
    return a+b
no = [1,2,3,4,5,6]
c = reduce(sum,no)
print(c)