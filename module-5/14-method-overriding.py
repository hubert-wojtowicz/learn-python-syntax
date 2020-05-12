class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 2

    def walk(self):
        print("walk")


m = Mammal()
# print(m.age) #AttributeError: 'Mammal' object has no attribute 'age'
print(m.weight)

f = Fish()
print(f.age)
print(f.weight)
