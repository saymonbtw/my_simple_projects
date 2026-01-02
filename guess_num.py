from random import *

def get_valid_num():
    while True:
        user_input = input(f"Введите число от 1 до {num_limit} ")
        if user_input.isdigit():
            num = int(user_input)
            if 1 <= num:
                return num
        print("Некорректный ввод. Попробуйте еще раз")

def get_limit_num():
    while True:
        limit = input("Введите предел загаданного числа -> ")
        if limit.isdigit():
            limit = int(limit)
            if limit > 1:
                return limit
        print("Некорректный ввод, давай еще раз!")

def show_menu():
    print("1) Правила игры")
    print("2) Начать играть")
    print("0) Выход")

print("Добро пожаловать в числовую угадайку!")


while True:
    show_menu()
    user_choise = input("Введите пункт меню -> ")

    if user_choise == "1":
        print("Программа загадала Вам целое число по Вашему выбору, Вам нужно его угадать!", "Удачи!", sep = "\n")

    elif user_choise == "2":
        attemps = 0
        num_limit = get_limit_num()
        secret_num = randint(1, num_limit)
        user_num = get_valid_num()

        while user_num != secret_num:
            if user_num > secret_num:
                print("Загаданное число меньше")
            else:
                print("Загаданное число больше")
            user_num = get_valid_num()
            attemps += 1
        print(f"Ты угадал за {attemps} попыток! ")

    elif user_choise == "0":
        print("Пока!")
        break

    else:
        print("Неверный пункт меню")