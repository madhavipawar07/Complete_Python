class person:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def show(self):
        print (f"The name is:{self.name}")
        print(f"The age is: {self.age}")

class programmer(person):
    def __init__(self,id):
        person.show()
        self.id = id 

    def show(self):
        print(f"The id is: {self.id}")

class developer(person):
    def __init__(self):
        programmer.show()

    def  show(self):
        print("This is a developer class")


class employee( programmer, developer):
    def __init__(self,address):
        developer.show(self)
        self.address = address

    def show(self):
        print(f"The address is : {self.address}")

e = employee("Pune")
e.show()