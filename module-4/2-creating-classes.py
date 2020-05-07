# use Pascal naming convention for classes
class MyPoint:
    def draw(self):
        print("draw")
        
point = MyPoint()
point.draw()
print(type(point))
print(isinstance(point, MyPoint))# True
print(isinstance(point, int))# False