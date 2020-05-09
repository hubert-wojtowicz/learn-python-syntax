from abc import ABC, abstractclassmethod


class UIControl(ABC):
    @abstractclassmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(controls):
    for ctrl in controls:
        ctrl.draw()


draw([DropDownList(),  TextBox(), DropDownList(), DropDownList()])
