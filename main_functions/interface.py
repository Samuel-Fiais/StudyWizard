# Import modules
from datetime import datetime
from os import system
from time import sleep
from main_functions.myjson import manipulate_json_file

user_interface = "root"
PASSWORD = ""
FILE_DATA = "../src/login/login.json"


def update_screen():
    system('clear')
    date = datetime.now()
    date_format = date.strftime("%d/%m %H:%M")
    print("-" * 50)
    print(f"{user_interface:<20}{date_format:>30}")


def login():
    while True:
        user = input("Username: ").strip()
        if user == user_interface:
            while True:
                password = input("Password: ").strip()
                if password == PASSWORD:
                    return True
                else:
                    print("Wrong password")
                    return False
        else:
            print("Wrong username")
            return False


def register():
    user = input("Username: ").strip()
    password = input("Password: ").strip()
    data_user = {
        "user": user,
        "password": password
    }
    manipulate_json_file(FILE_DATA, "a", data_user)
    print("User registered")
    global user_interface
    user_interface = user
    sleep(2)
    update_screen()
    login()


def main_menu():
    update_screen()
    while True:
        print("""Select an option: 
    [1] Login
    [2] Register
    [3] Exit""")
        option = input(">> ").strip()
        if option == "1":
            login()
            update_screen()
        elif option == "2":
            register()
            update_screen()
        elif option == "3":
            exit()
        else:
            print("Invalid option")
            update_screen()


main_menu()
