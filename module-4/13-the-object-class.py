class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def walk(self):
        print("walk")


m = Mammal()
print(isinstance(m, Animal))
print(isinstance(m, object))
print(isinstance(m, Fish))

print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))
print(issubclass(Animal, Mammal))
