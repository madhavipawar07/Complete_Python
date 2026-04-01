class employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id


    def showdetails(self):
        print(f"The employee name: {self.id} is {self.name}")


class programmer(employee):
        def showlanguage(self):
            print("The default language is python")


e1 = employee("Harry",400)
e1.showdetails()
e2 = programmer("alice",402)
e2.showlanguage()

