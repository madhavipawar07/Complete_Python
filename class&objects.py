#Using class
class simple:
    name = "Riya"
    age = 9

obj = simple()
print(obj.name)

print(obj.age)


#Using self parameter 
class person:
    name = "Harry"
    age = 20
    occupation = "Software developer"
    networth = 10

    def info (self):
        print(f"{self.name} is a {self.occupation}")

a=person()
b=person()
c=person()

b.name = "shubham"
b.occupation = "HR"

a.name = "Alice"

a.info()
b.info()
c.info()


class details:
    name = "Rohan"
    age = 20

    def desc(self):
        print(f"{self.name} is {self.age} years old")


obj = details()
obj.desc()