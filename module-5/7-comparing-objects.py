
class Point:
    default_color = "red"

    def __init__(self, x, y):  # magic method __xxx__()
        # self is refernce to current object
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __eq__(self, another):
        return self.x == another.x and self.y == another.y


point1 = Point(1, 2)
point2 = Point(1, 2)
# Fasle as comparing reference address value by default when magic __eq__ overriden it will use custom comparision instead
print(point1 == point2)
