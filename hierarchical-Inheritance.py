class Person:
    def __init__(self, name):
        self.name = name

    def showName(self):
        print(f"Name: {self.name}")


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def showStudent(self):
        self.showName()
        print(f"Course: {self.course}")


class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

    def showEmployee(self):
        self.showName()
        print(f"Employee ID: {self.emp_id}")


s = Student("Madhavi", "Computer Engineering")
e = Employee("Rahul", 101)

s.showStudent()
e.showEmployee()