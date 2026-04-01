class vehicle:
    def start(self):
        print("vehicle is starting")

class bike(vehicle):
    def start(self):
        print("Bike starts with self start button")

class car(vehicle):
    def start(slef):
        print("Car starts with key")

b = bike()
c = car()
b.start()
c.start()

# Using super() 
class employee:
    def work(self):
        print("Employee is working")

class developer(employee):
    def work(self):
        super().work()
        print("Developer is writing code")

d = developer()
d.work()