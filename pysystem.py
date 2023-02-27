import os

menu = {
    "1": "Удаление ненужных пакетов в Arch Linux",
    "2": "Обновление системы Arch Linux через yay",
    "3": "Freerdp",
    "4": "Выход"
}

while True:
    os.system("clear")  # Очистка экрана перед выводом меню
    print("Меню:")
    for key, value in menu.items():
        print(f"{key}. {value}")

    choice = input("Выберите действие (1-4): ")

    if choice == "1":
        print("Вы выбрали удаление ненужных пакетов в Arch Linux")
        os.system("sudo pacman -Rns $(pacman -Qtdq)")
    elif choice == "2":
        print("Вы выбрали обновление системы Arch Linux через yay")
        os.system("yay -Syu")
    elif choice == "3":
        print("Вы выбрали Freerdp")

        # Выводим подменю из файлов bash в папке freerdp
        sub_menu = [f for f in os.listdir("freerdp") if f.endswith('.sh')]
        #os.listdir("freerdp")
        sub_menu.sort()
        while True:
            os.system("clear")  # Очистка экрана перед выводом подменю
            print("Подменю Freerdp:")
            for i, item in enumerate(sub_menu):
                print(f"{i+1}. {item}")

            print("q- выход из подменю Freerdp")
            sub_choice = input("Выберите действие (1-{}): ".format(len(sub_menu)))

            if sub_choice.isdigit() and 1 <= int(sub_choice) <= len(sub_menu):
                script_path = os.path.join("freerdp", sub_menu[int(sub_choice)-1])
                os.system(f"bash {script_path}")
            elif sub_choice == "q":
                print("Выход из подменю Freerdp...")
                break
            else:
                print("Неверный выбор. Попробуйте ещё раз.")

    elif choice == "4":
        print("Выход из программы...")
        break
    else:
        print("Неверный выбор. Попробуйте ещё раз.")
