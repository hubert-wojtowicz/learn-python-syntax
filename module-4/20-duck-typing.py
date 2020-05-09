class TextBox:
    def draw(self):
        print("TextBox")


class DropDownList:
    def draw(self):
        print("DropDownList")

# this feature  pulimorphism without base classes and inheritacnae is called Duck Typing


def draw(controls):
    for ctrl in controls:
        ctrl.draw()


draw([DropDownList(),  TextBox(), DropDownList(), DropDownList()])
