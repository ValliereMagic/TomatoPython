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

    def describe(self):
        return ("\n" + self.__class__.__name__ + " name: " + self.get_name().capitalize() + "\n" +
                self.__class__.__name__ + " nationality: " + self.get_nationality().capitalize() + "\n")

    @classmethod
    def input_attributes(cls):
        return input("Enter the name of the fruit: ").lower(), input("Enter the nationality of the fruit: ").lower()


class Colourable(Fruit):
    def __init__(self, name, nationality, colour):
        super(Colourable, self).__init__(name, nationality)
        self.__colour = colour

    def get_colour(self):
        return self.__colour

    def describe(self):
        return super(Colourable, self).describe() + \
               self.__class__.__name__ + " colour: " + self.get_colour().capitalize() + "\n"

    @classmethod
    def input_attributes(cls):
        return (*super(Colourable, cls).input_attributes()), input("Enter the colour of the fruit: ").lower()


class FruitList(list):
    def __init__(self):
        super(FruitList, self).__init__()

    def __str__(self):
        descriptions = ""

        for fruit in self:
            descriptions += fruit.describe()

        return descriptions

    def create_fruit(self):
        try:
            import Varieties
            variety = getattr(Varieties, input("Enter the type of fruit: ").capitalize())
            self.append(variety(*variety.input_attributes()))
            print("Added new " + variety.__name__ + " successfully.")
        except AttributeError:
            print("Invalid fruit type")

    def remove_fruit(self, name):
        fruit = self.get_fruit(name)

        if fruit:
            self.remove(fruit)
            print(fruit.__class__.__name__ + " " + name + " removed successfully.")
        else:
            print("Failed to remove Fruit " + name)

    def describe_fruit(self, name):
        fruit = self.get_fruit(name.lower())

        if fruit:
            print(fruit.describe())
        else:
            print("Fruit " + name + " not found.")

    def get_fruit(self, name):
        for fruit in self:
            if fruit.get_name() == name:
                return fruit
        return None
