class person :
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    @classmethod
    def from_string(cls, string):
        name,age = string.split(",")
        return cls(name, int(age))
    
person1 = person.from_string("John doe",30)
print(person1.name,person.age)

p = person("Alice",64)
p.from_string()