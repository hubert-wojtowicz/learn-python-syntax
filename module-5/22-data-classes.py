from collections import namedtuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)

print(id(p1))
print(id(p2))
print(p1 == p2)


p3 = Point2(1, 2)
p4 = Point2(1, 2)

print(id(p3))
print(id(p3))
print(p3 == p4)

PointSpecial = namedtuple("PointSpecial", ["x", "y"])
p5 = PointSpecial(x=1, y=2)
p6 = PointSpecial(x=1, y=2)
print(id(p5))
print(id(p6))
print(p5 == p6)
