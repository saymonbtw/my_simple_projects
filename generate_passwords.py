from random import *

def generate_password(lenght, symbols):
    return "".join([choice(symbols) for _ in range(lenght)])

digits = "0123456789"
lowcase_tetters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
ambiguous = "il1Lo0O"
chars = ""

cnt_passwords = int(input("Введите кол-во паролей для генерации "))
len_password = int(input("Укажите длину пароля "))
need_digit = input("Включать ли цифры? (y/n) ")
need_upcase = input("Включать ли прописные буквы? (y/n) ")
need_lowcase = input("Включать ли строчные буквы? (y/n) ")
need_punc = input("Включать ли символы? (y/n) ")
del_amb_symbols = input("Исключать ли неоднозначные символы il1Lo0O? (y/n) ")

if need_digit == "y": chars += digits
if need_lowcase == "y": chars += lowcase_tetters
if need_upcase == "y": chars += uppercase_letters
if need_punc == "y": chars += punctuation
if del_amb_symbols == "y": chars
if del_amb_symbols == "y":
    chars = ''.join([c for c in chars if c not in ambiguous])

for _ in range(cnt_passwords):
    print(generate_password(len_password, chars))