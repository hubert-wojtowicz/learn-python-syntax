class Point:
    def __init__(self, x, y): # magic method __xxx__()
        # self is refernce to current object
        self.x = x
        self.y = y
        
    def draw(self):
        print("({}, {})".format(self.x, self.y))
        
point = Point(1, 2)
point.draw()