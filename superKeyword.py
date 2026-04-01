class parentClass:
    def parent_method(self):
        print("This is a parent method")


class child_class(parentClass):
    def child_method(self):
        print("This is a child method")
        super().parent_method

c = child_class()
c.child_method()

#Using Constructor

class employee:
    def __init__(self,name, id):
        self.name = name
        self.id = id

class person(employee):
    def __init__(self,lan,name, id):
        super().__init__(name, id)
        self.lan = lan
 
p = person("Python","Rahul", 4000)
print(p.name)
print(p.id)
print(p.lan)


#__init__ is a dunder method, which is used to initialize the attributes of a class. It is called when an object of the class is created. The super() function is used to call the parent class's __init__ method, which allows us to initialize the attributes of the parent class in the child class.


#__str__ is a dunder method, which is used to return a string representation of an object. It is called when we print an object or when we use the str() function on an object. We can override this method in our class to provide a custom string representation of our objects.


#__repr__ is a dunder method, which is used to return a string representation of an object that is unambiguous and can be used to recreate the object. It is called when we use the repr() function on an object. We can override this method in our class to provide a custom string representation of our objects that can be used for debugging purposes.


#__call__ is a dunder method, which is used to make an object callable. It is called when we call an object as if it were a function. We can override this method in our class to provide a custom behavior when an object is called.


#__len__ is a dunder method, which is used to return the length of an object. It is called when we use the len() function on an object. We can override this method in our class to provide a custom behavior when the len() function is called on our objects.