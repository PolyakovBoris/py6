"""
Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
"""


def quizz(question: str = '2 + 2', tries: list = ('2', '4'), tries_count=5) -> int:
    while True:
        user_input = input(question + '?')
        if user_input in tries:
            print('you are right')
            return tries_count
        else:
            tries_count -= 1
            if tries_count == 0:
                return tries_count
