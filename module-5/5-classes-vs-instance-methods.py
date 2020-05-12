class Point:
    default_color = "red"

    def __init__(self, x, y):  # magic method __xxx__()
        # self is refernce to current object
        self.x = x
        self.y = y

    def draw(self):
        print("({}, {})".format(self.x, self.y))

    # class methods
    @classmethod  # decorator makes difference
    def zero(cls):  # cls is pure convention - can be used anythink
        return cls(0, 0)


# Point.zero() # factory method
Point.zero().draw()
