class Math:
    def __init__(self,num):
        self.__num = num

    def show(self):
        print(f"The value of number is: {self.num}")

    @staticmethod
    def add(a,b):
        return a+b

m = Math(6)
print(m._Math__num)

print(Math.add(4,5))