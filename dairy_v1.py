"""
программа, куда пользователь вводит задачу и время,
а скрипт отслеживает, когда напомнить.
"""

from datetime import datetime

pattern = "%H:%M"


def menu():
    print("1) Добавить задачу и время")
    print("2) Отследить текущие задачи")
    print("3) Выход")


while True:
    menu()

    user_choice = int(input("Введите пункт меню: "))
    while user_choice not in [1, 2, 3]:
        menu()
        user_choice = int(input("Введен неправильный пункт меню, попробуйте еще раз: "))

    if user_choice == 3:
        print("Пока!")
        break

    elif user_choice == 1:
        with open("dates.txt", "a", encoding="utf-8") as user_file:
            new_task = input("Введите новую задачу: ")
            new_time = input("Введите время (в формате ЧЧ:ММ): ")
            user_file.write(f"{new_task} {new_time}\n")
    else:
        with open("dates.txt", "r", encoding="utf-8") as user_file:
            for line in user_file:
                action = line.split()[0]
                user_time = datetime.strptime(line.split()[-1].strip(), pattern)
                time_now = user_time.replace(
                    hour=datetime.now().hour, minute=datetime.now().minute
                )

                if time_now > user_time:
                    delta = time_now - user_time
                    delta_hours = int(delta.total_seconds() // 3600)
                    delta_minutes = int((delta.total_seconds() // 60) % 60)
                    print(f"Ты опоздал {action}")
                    print(
                        f"Это нужно было сделать {delta_hours} часов {delta_minutes} минут назад"
                    )
                    print()
                elif time_now < user_time:
                    delta = user_time - time_now
                    delta_hours = int(delta.total_seconds() // 3600)
                    delta_minutes = int((delta.total_seconds() // 60) % 60)
                    print(
                        f"{action} нужно сделать через {delta_hours} часов и {delta_minutes} минут"
                    )
                    print()
