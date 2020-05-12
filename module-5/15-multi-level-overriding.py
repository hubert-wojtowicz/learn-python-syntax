class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


# inheritacje abuse
class Chicken(Bird):
    pass
