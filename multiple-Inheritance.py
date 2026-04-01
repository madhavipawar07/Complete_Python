class employee:
    def __init__(self,name):
        self.name = name

    def show(self):
        print("The name is {self.name}")

class dancer:
    def __init__(self,dance):
        self.dance = dance

    def show(self):
        print("The dance is {self.dance}")

class dancerEmployee(employee, dancer):
    def __init__(self,dance, name):
        self.dance = dance 
        self.name = name

    # def show(self):
    #     print(f"{self.name} can do {self.dance}")

obj = dancerEmployee("Kathak", "Madhavi")
print(obj.name)
print(obj.dance)