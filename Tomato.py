class Tomato:
    __tomato_name = None
    __tomato_colour = None
    __tomato_nationality = None

    def __init__(self, tomato_name, tomato_colour, tomato_nationality):
        if tomato_name is not None and tomato_colour is not None and tomato_nationality is not None:
            self.__tomato_name = tomato_name
            self.__tomato_colour = tomato_colour
            self.__tomato_nationality = tomato_nationality

    def get_name(self):
        if self.__tomato_name is not None:
            return self.__tomato_name

    def get_colour(self):
        if self.__tomato_colour is not None:
            return self.__tomato_colour

    def get_tomato_nationality(self):
        if self.__tomato_nationality is not None:
            return self.__tomato_nationality
