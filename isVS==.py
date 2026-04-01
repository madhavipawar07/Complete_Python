a = [1,2,3,4]
b = [1,2,3,4]

print(a is b) #Checks the exact location of obj in memory
print(a==b) #checks the values of variables

a= 6 #strings and integers are immutable so memory loc is same
b =6

print(a is b)
print(a==b)