#---------dir()----------

x = [1,2,3]
print(dir(x))

#-------dict_attribute---------

class person:
    def __init__(self,name,age,dept):
        self.name = name
        self.age = age
        self.dept = dept

p = person("Rahul", 4000, "IT")
print(p.__dict__)

#-------help()---------------

print(help(person))