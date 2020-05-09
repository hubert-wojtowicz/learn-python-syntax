from abc import ABC, abstractclassmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False

    @abstractclassmethod
    def read(self):
        pass


class File(Stream):
    def read(self):
        print("Reading data from a file...")


class Network(Stream):
    def read(self):
        print("Reading data from a network...")


class MemoryStream(Stream):
    pass


"""
s = Stream() #TypeError: Can't instantiate abstract class Stream with abstract methods read
s.open()
"""
# the same here as not overriding abstract method means we still deal with abstract type
# TypeError: Can't instantiate abstract class MemoryStream with abstract methods read
"""
ms = MemoryStream()
ms.open()
"""
