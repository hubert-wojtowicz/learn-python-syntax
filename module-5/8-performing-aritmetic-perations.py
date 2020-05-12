class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


point1 = Point(1, 1)
point2 = Point(2, 3)
print(point1)
print(point2)
print(point1 + point2)
