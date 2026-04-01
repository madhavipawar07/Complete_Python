tup = (1,2,78,32)
print(type(tup),tup)

# all list methods can be applied to tuples

#operations on tuple
#tuples are immutable hence if we want to change it, convert it into list and then perform operations and then convert back to list
countries = ["Spain", "Italy", "India", "England" , "Germany"]
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[3]="China"
countries = tuple(temp)
print(countries)

#However two tuples can be concatenated without converting them to list
countries = ["Pakistan", "Bangladesh", "Shrilanka","Afganistan"]
countries1= ["India", "America", "China","India"]
countries2 = countries + countries1
print(countries2)

#Tuple methods
print(countries1.count("India"))

print(len(countries))

