class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def getSalary(self):
        print(self.salary)
    def hello():
        print("Hello world")
    
rohan=Employee("Rohan", "3455")
rohan.getSalary()
Employee.hello()
