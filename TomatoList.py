import Tomato


class TomatoList(list):

    def __init__(self):
        super(TomatoList, self).__init__()

    @staticmethod
    def make_new_tomato():
        print("Enter a new tomato to add to the tomato class \n")

        print("Enter the name of the tomato: \n")
        tomato_name = input()

        print("Enter the colour of the tomato: \n")
        tomato_colour = input()

        print("Enter the nationality of the tomato: \n")
        tomato_nationality = input()

        return Tomato.Tomato(tomato_name, tomato_colour, tomato_nationality)

    def delete_tomato(self, tomato_name):
        tomato_to_delete = self.get_tomato(tomato_name)

        if tomato_to_delete is not None:
            self.remove(tomato_to_delete)
            print("Deleted: " + tomato_name + " successfully.")

        else:
            print("Failed to delete: " + tomato_name + ".")

    def list_all_tomatoes(self):
        for tomato in self:
            print("Tomato Name: " + tomato.get_name() + "\n" +
                  "Tomato Colour: " + tomato.get_colour() + "\n" +
                  "Tomato Nationality: " + tomato.get_tomato_nationality() + "\n")

    def describe_tomato(self, tomato_name):
        tomato = self.get_tomato(tomato_name)

        if tomato is not None:
            print("Tomato Colour: " + tomato.getColour() + "\n" +
                  "Tomato Nationality: " + tomato.getTomatoNationality())

    def get_tomato(self, tomato_name):

        for tomato in self:

            if tomato.get_name() == tomato_name:
                return tomato

        return None
