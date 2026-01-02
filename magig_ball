from random import randint, choice
from time import sleep


def get_user_answer():
    while True:
        user_answer = input("Еще есть вопросы? (да/нет) ")
        if user_answer.lower().strip() in ["да", "нет"]:
            return user_answer
        print("Нужен четкий ответ! да или нет...")


def get_question():
    while True:
        user_question = input()
        if not user_question.endswith("?"):
            print("Это не не очень похоже на вопрос...", "Попробуй еще раз", sep="\n")
            continue
        return user_question


answers = [
    "Бесспорно",
    "Мне кажется - да",
    "Пока неясно, попробуй снова",
    "Даже не думай",
    "Предрешено",
    "Вероятнее всего",
    "Спроси позже",
    "Мой ответ - нет",
    "Никаких сомнений",
    "Хорошие перспективы",
    "Лучше не рассказывать",
    "По моим данным - нет",
    "Можешь быть уверен в этом",
    "Да",
    "Сконцентрируйся и спроси опять",
    "Весьма сомнительно",
]

print("Здравствуй, я магический шар и я знаю ответ на любой твой вопрос!")
user_name = input("Как я могу к тебе обращаться? ")

while True:
    print(f"Хорошо, {user_name}, какой у тебя вопрос? ")
    user_quest = get_question()

    print("Секунду...")
    sleep(randint(1, 3))
    print(choice(answers))

    user_ans = get_user_answer()
    if user_ans == "да":
        continue
    else:
        print("Если будут вопросы - возвращайся!")
        break