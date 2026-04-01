#Public access Modifiers/specifiers

class Employee:
    def __init__(self):
        self.name = "harry"

a= Employee()
print(a.name)

#Private Access Modifiers

class employee:
    def __init__(self):
        self.__name= "Alice"

b = employee()
#print(b.__name) #cannot accessed directly
print(b._employee__name) # accessed indirectly using name mangling


#Protected Access Modifier

class employee:
    def __init__(self):
        self._name = "Rohan" #Protected variable

    def _funName(self): #Protected Method
        return "CodeWithHarry"
    
class subject(employee):
    pass
    
c = employee()
e = subject()
print(c._name)
print(c._funName())

print(e._name)
print(e._funName())

