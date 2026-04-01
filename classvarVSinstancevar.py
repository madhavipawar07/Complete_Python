#CLASS_VARIABLES
class myclass:
    class_var = 0

    def __init__(self):
        myclass.class_var+=1

    def print_class(self):
        print(myclass.class_var)

c = myclass()
c.print_class()
c1= myclass()
c1.print_class()


#INSTANCE_VARIABLES
class myclass:
    def __init__(self,name):
        self.name = name

    def print_name(self):
        print(self.name)

obj = myclass("Harry")
obj.print_name()