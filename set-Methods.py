info = {"Carla", 19, False, 5, 9}
print(info)

s = {1,2,4,7}
s1={5,2,3,6}
print(s.union(s1))

s.update(s1)
print(s,s1)

s = set()
print(type(s))

#Accessing set items
info = {"Carla", 19, False, 5.9, 19}
for value in info :
    print(value)

#Union & Union_update
s1 = { 1,2,5,6}
s2 = {3, 6, 7}
print(s1.union(s2))

print(s1.update(s2))
print(s1,s2)

#Intersection & intersection_update
cities = {"Tokyo", "Delhi", "Berlin", "Japan"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Delhi"}
cities3 = cities.intersection(cities2)
print(cities3)

cities.intersection_update(cities2)
print(cities)

#Symmetric_difference
cities3= cities.symmetric_difference(cities2)
print(cities3)


#difference &  difference_update
cities3= cities.difference(cities2)
print(cities3)

#built-in methods
#isdisjoint()
print(cities.isdisjoint(cities2))

#issuperset()
print(cities.issuperset(cities2))

#issubset()
print(cities.issubset(cities2))

#add()
cities.add("Mumbai")
print(cities)

#remove()
cities.remove("Tokyo")
print(cities)

#discard()
cities.discard("Bangal")
print(cities)

#pop()
item = cities.pop()
print(cities)
print(item)

# #del
# del cities

#clear()
cities.clear()
print(cities)

#Check if the item exists

info = {"carla", False , 3, 15 , 9.0}
if "carla" in info:
    print("It is present")
else:
    print("It is absent")




  