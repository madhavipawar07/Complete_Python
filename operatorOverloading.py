class number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return number(self.value + other.value)
    
    def __sub__(self,other):
        return number ( self.value - other.value)
    
    def __mul__(self,other):
        return number (self.value * other.value)
    
    def __str__(self):
        return str(self.value)
    
r1 = number(8)
r2 = number(4)

print(r1 + r2)
print(r1 - r2)
print(r1 * r2)
