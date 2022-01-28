from os import system
from datetime import datetime
from time import sleep

user = "root"
password = ""
menu = "Inicio"

def refresh_screen():
    current_day_time = datetime.now().strftime('%d/%m %H:%M')
    system("clear")
    print("=" * 65)
    print(f"| {user:<20} {menu:^15} {current_day_time:>24} |")
    print("=" * 65)
    print("")

def register():
    global menu 
    menu = "Registro"
    if user == "root":
        while True:
            name = str(input("Usuário: ")).strip()
            sleep(0.5)
            option = str(input(f"Quer continuar com o nome {name}? [S/N] ")).strip().upper()[0]
            sleep(1)
            if option == "S":
                while True:
                    password = str(input("Senha: "))
                    sleep(0.5)
                    option = str(input(f"Quer continuar com a senha {password}? [S/N] ")).strip().upper()[0]
                    sleep(1)
                    if option == "S":
                        print("\nCadastro Concluído com Sucesso!!")
                        return {
                            "name": name,
                            "password": password
                        }
                    elif option == "N":
                        refresh_screen()
                        print(">> Coloque outra senha! <<")
                        print(f"- Usuário: {name}\n")
                        sleep(0.5)
                    else:
                        refresh_screen()
                        print(">> Tentativa Inválida. Tente Novamente! <<")
                        print(f"- Usuário: {name}\n")
                        sleep(0.5)
            elif option == "N":
                refresh_screen()
                print(">> Coloque outro nome de usuário! <<\n")
                sleep(0.5)
            else:
                refresh_screen()
                print(">> Tentativa Inválida. Tente Novamente! <<\n")
                sleep(0.5)

def start_interface():
    refresh_screen()
    register()


start_interface()
