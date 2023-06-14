"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
Добавьте возможность запуска в терминале с передачей даты на проверку
"""
from sys import argv


LIST_31_DAYS_MONTHES = [1,3,5,7,8,10,12]
LIST_30_DAYS_MONTHES = [4,6,9,11]


def is_date_exist(user_date: str) -> bool:
    date, month, year = (user_date.split('.'))
    if (int(year) < 1) | (int(year) > 9999):        # проверка года
        print('incorrect year')
        return False
    elif (int(month) < 1) | (int(month) > 12):      # проверка месяца
        print('incorrect month')
        return False
    elif (int(date) < 1) | (int(date) > 31):        # проверка количества дней
        print('incorrect date')
        return False
    elif int(date) == 28 | int(date) == 29:         # проверка дней в високосных годах и феврале с вызовом функции
        if check_visokos_year(int(date), int(year)) is False:
            print('incorrect visokos year')
            return False
    elif (int(date) == 31) & (int(month) not in LIST_31_DAYS_MONTHES):      # проверка 31 день
        print('incorrect count of days in month')
        return False
    elif (int(date) == 30) & (int(month) not in LIST_30_DAYS_MONTHES):      # проверка 30 дней
        print('incorrect count of days in month')
        return False
    return True

def check_visokos_year(date: int, year: int) -> bool:
    if (date == 29) & (year % 4 != 0):
        return False
    elif (date == 28) & (year % 4 == 0):
        return False

if __name__ == '__main__':
    if len(argv) > 1:
        print(is_date_exist(argv[1]))           # запуск из терминала с аргументами
else:
    print(is_date_exist('30.01.2009'))
