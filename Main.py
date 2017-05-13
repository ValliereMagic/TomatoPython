import Tomato

tomatoList = []


def makeNewTomato():
    print("Enter a new tomato to add to the tomato class \n")

    print("Enter the name of the tomato: \n")
    tomatoName = input()

    print("Enter the colour of the tomato: \n")
    tomatoColour = input()

    print("Enter the nationality of the tomato: \n")
    tomatoNationality = input()

    return Tomato.Tomato(tomatoName, tomatoColour, tomatoNationality)


def printInstructions():
    print("Enter the number of an option to complete a task: \n"
          "1.) Add a new tomato to the system \n"
          "2.) Remove a tomato from the system \n"
          "3.) Print all the tomatoes that exist in the system \n"
          "4.) Print the description of a specific tomato \n"
          "5.) Print the Instructions again \n"
          "6.) Close the program")


def deleteTomato(tomatoName):
    tomatoToDelete = getTomato(tomatoName)

    if tomatoToDelete is not None:
        tomatoList.remove(tomatoToDelete)
        print("Deleted: " + tomatoName + " successfully.")

    else:
        print("Failed to delete: " + tomatoName + ".")


def listAllTomatoes():
    for tomato in tomatoList:
        print("Tomato Name: " + tomato.getName() + "\n" +
              "Tomato Colour: " + tomato.getColour() + "\n" +
              "Tomato Nationality: " + tomato.getTomatoNationality() + "\n")


def describeTomato(tomatoName):
    tomato = getTomato(tomatoName)

    if tomato is not None:
        print("Tomato Colour: " + tomato.getColour() + "\n"
                                                       "Tomato Nationality: " + tomato.getTomatoNationality())


def getTomato(tomatoName):
    for tomato in tomatoList:
        if tomato.getName() == tomatoName:
            return tomato
    return None


def main():
    printInstructions()
    namePrompt = "Name of the tomato: \n"

    while True:
        option = int(input())

        if option == 1:
            tomato = makeNewTomato()

            if tomato is not None:
                tomatoList.append(tomato)
                print("Created new tomato: " + tomato.getName() + " successfully.")

            else:
                print("Failed to create new tomato.")

        elif option == 2:
            deleteTomato(str(input(namePrompt)))

        elif option == 3:
            listAllTomatoes()

        elif option == 4:
            describeTomato(str(input(namePrompt)))

        elif option == 5:
            printInstructions()

        elif option == 6:
            break


main()
