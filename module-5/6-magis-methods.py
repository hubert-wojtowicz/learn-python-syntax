class Point:
    default_color = "red"

    def __init__(self, x, y):  # magic method __xxx__()
        # self is refernce to current object
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    # class methods
    @classmethod  # decorator makes difference
    def zero(cls):  # cls is pure convention - can be used anythink
        return cls(0, 0)


point = Point(1, 2)
print(point)  # here is used overriden implementation
