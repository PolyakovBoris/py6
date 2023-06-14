"""
задача о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел
для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и
выведите 4 успешных расстановки.
"""
import time
from random import randrange

def check_horizontal_crossing(field, x):

    for i in field[x]:
        if (i > 0):
            return False
    return True

def check_vertical_crossing(field, y):
    for i in range(FIELD_SIZE_Y):
        if field[i][y] > 0:
            return False
    return True

def check_diagonal_crossing(field, x,y):
    for i in range(x, 7):
        for j in range(y, 7):
            if (field[i][j] > 0):
                return False
    return True


FIELD_SIZE_X = 8
FIELD_SIZE_Y = 8
COUNT_OF_FIGURES = 8
field = []
x: int
y: int
counter = 0

field = [[0 for x in range(FIELD_SIZE_X)] for y in range(FIELD_SIZE_Y)]
counter = 0
while counter < COUNT_OF_FIGURES:
    x = randrange(0,8)
    y = randrange(0,8)

    if (field[x][y] == 0):
        if check_horizontal_crossing(field, x) is True:
            if check_vertical_crossing(field, y) is True:
                print(x,y)
                if check_diagonal_crossing(field, x, y) is True:
                    field[x][y] = 1
                    counter += 1
                    print(f'добавлена фигура {counter} x= {x} y = {y}')
                    time.sleep(0.5)
                    for i in field:
                        print(i)

for i in field:
    print(i)