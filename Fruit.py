class Fruit(object):
    __name = None
    __nationality = None

    def __init__(self, name, nationality):
        self.__name = name
        self.__nationality = nationality

    def get_name(self):
        return self.__name

    def get_nationality(self):
        return self.__nationality


class Colourable(Fruit):
    def __init__(self, name, colour, nationality):
        super(Colourable, self).__init__(name, nationality)
        self.__colour = colour

    def get_colour(self):
        return self.__colour

class FruitList(list):
    def __init__(self):
        super(FruitList, self).__init__()

    def add(self, type):

