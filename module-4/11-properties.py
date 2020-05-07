class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        self.__price

    # this is optional - not implementing this will give readonly property
    @price.setter
    def price(self, value):
        if (value < 0):
            raise ValueError("Price can not be negative (new implementation).")
        self.__price = value


class ProductOldImpl:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        self.__price

    def set_price(self, value):
        if (value < 0):
            raise ValueError("Price can not be negative.")
        self.__price = value

    price = property(get_price, set_price)


# how to prevent this - to have more control over object
product = Product(20)
# this will use property object
product.price = -20
