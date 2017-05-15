import TomatoList

tomato_list = TomatoList.TomatoList()


def print_instructions():
    print("Enter the number of an option to complete a task: \n"
          "1.) Add a new tomato to the system \n"
          "2.) Remove a tomato from the system \n"
          "3.) Print all the tomatoes that exist in the system \n"
          "4.) Print the description of a specific tomato \n"
          "5.) Print the Instructions again \n"
          "6.) Close the program")


def main():
    print_instructions()
    name_prompt = "Name of the tomato: \n"

    while True:
        option = int(input())

        if option == 1:
            tomato = tomato_list.make_new_tomato()

            if tomato is not None:
                tomato_list.append(tomato)
                print("Created new tomato: " + tomato.get_name() + " successfully.")

            else:
                print("Failed to create new tomato.")

        elif option == 2:
            tomato_list.delete_tomato(str(input(name_prompt)))

        elif option == 3:
            tomato_list.list_all_tomatoes()

        elif option == 4:
            tomato_list.describe_tomato(str(input(name_prompt)))

        elif option == 5:
            print_instructions()

        elif option == 6:
            break

if __name__ == "__main__":
    main()
