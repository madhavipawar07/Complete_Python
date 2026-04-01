class myclass:
    def __init__(self, value):
        self.value = value

    def show(self):
        print(f"Value is {self.value}" )

    @property #getter
    def ten_value(self):
        return 10 * self.value
    
    @ten_value.setter
    def ten_value(self, newvalue):
        self.value = newvalue/10
    
obj = myclass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()
    