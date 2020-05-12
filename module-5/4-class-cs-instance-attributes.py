class Point:
    default_color = "red"

    def __init__(self, x, y):  # magic method __xxx__()
        # self is refernce to current object
        self.x = x
        self.y = y

    def draw(self):
        print("({}, {})".format(self.x, self.y))


point = Point(1, 2)
point.draw()

point2 = Point(3, 4)
point2.draw()  # it will draw instance attributes
# but there can be class level attributes - sth similar to static

print(id(point.default_color))
print(id(point2.default_color))

print(point.default_color)
print(point2.default_color)

point.default_color = "blue";
print(point.default_color)
print(point2.default_color)
