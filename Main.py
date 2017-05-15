import TomatoList
import sqlite3
import pickle


class Main:

    def __init__(self):
        self.tomato_list = TomatoList.TomatoList()
        self.sqlite_db = None

        self.run()

    @staticmethod
    def print_instructions():
        print("Enter the number of an option to complete a task: \n",
              "1.) Add a new tomato to the system \n",
              "2.) Remove a tomato from the system \n",
              "3.) Print all the tomatoes that exist in the system \n",
              "4.) Print the description of a specific tomato \n",
              "5.) Print the Instructions again \n",
              "6.) Load data from tomato.db \n",
              "7.) Dump data to tomato.db \n",
              "8.) Delete old database and initialize a new one \n",
              "9.) Close the program")

    @staticmethod
    def connect_db():
        rv = sqlite3.connect("db/tomato.db")
        rv.row_factory = sqlite3.Row
        return rv

    def get_db(self):
        if self.sqlite_db is None:
            self.sqlite_db = self.connect_db()
        return self.sqlite_db

    def close_db(self, error=None):
        if error:
            print(error)
        if self.sqlite_db is not None:
            self.sqlite_db.close()

    def init_db(self):
        db = self.get_db()
        with open("db/schema.sql", "r") as f:
            db.cursor().executescript(f.read())
        db.commit()

        print("Database Initialized.")

    @staticmethod
    def serialize_object(obj):
        return pickle.dumps(obj)

    @staticmethod
    def deserialize_object(bytes_obj):
        return pickle.loads(bytes_obj)

    def load_from_db(self):
        db = self.get_db()
        cursor = db.execute("SELECT data FROM tomatoes ORDER BY id")
        data = cursor.fetchone()

        self.tomato_list = self.deserialize_object(data[0])

        print("Loaded TomatoList from database.")

    def dump_to_db(self):
        db = self.get_db()
        data = self.serialize_object(self.tomato_list)

        db.execute("INSERT INTO tomatoes (data) VALUES (?)", [data])
        db.commit()

        print("TomatoList saved to database.")

    def run(self):
        self.print_instructions()
        name_prompt = "Name of the tomato: \n"

        while True:
            option = int(input())

            if option == 1:
                tomato = self.tomato_list.make_new_tomato()

                if tomato is not None:
                    self.tomato_list.append(tomato)
                    print("Created new tomato: " + tomato.get_name() + " successfully.")

                else:
                    print("Failed to create new tomato.")

            elif option == 2:
                self.tomato_list.delete_tomato(str(input(name_prompt)))

            elif option == 3:
                self.tomato_list.list_all_tomatoes()

            elif option == 4:
                self.tomato_list.describe_tomato(str(input(name_prompt)))

            elif option == 5:
                self.print_instructions()

            elif option == 6:
                self.load_from_db()

            elif option == 7:
                self.dump_to_db()

            elif option == 8:
                self.init_db()

            elif option == 9:
                break


if __name__ == '__main__':
    Main()
