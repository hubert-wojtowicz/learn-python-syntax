class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


# bad practice but ilustrative
class Manager(Employee, Person):
    pass


class Manager2(Person, Employee):
    pass


m = Manager()
m.greet()


m2 = Manager2()
m2.greet()
