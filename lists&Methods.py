marks = [3,5,6,"Harry", True]
print(marks[2])
print(marks[0])

#Negative indexing
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
print(colors[:])
print(colors[-5])
print(colors[-3])

#Checking if the given item is present in the list or not
if 6 in marks:
    print("yes")
else:
    print("No")


#printing a range of list items 
print(marks[1:0])
print(marks[0:1])
print(marks[3:3])
print(marks[2:6])
print(marks[1:4:2])
print(marks[1:5:3])

l= [11,45,1,2,4,6,8]
print(l)

l.append(7)
print(l)

l.sort(reverse=True) #sorts list according to descending order
print(l)

l.sort()
print(l)

print(l.index(11))

print(l.count(1))

m=l.copy()
print(m)

l.insert(1,899)
print(l)

m=[900,100,1200]
l.extend(m)
print(l)

#using concatenate
# k=l+m
# print(k)

