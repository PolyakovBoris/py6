from random import randint as rndint


def find_num(start: int = 0, end: int = 10, attempts_count: int = 5) -> bool:
    num = rndint(start, end)
    user_input = None
    while user_input != num:
        attempts_count -= 1
        if attempts_count == 0:
            return False
        user_input = input(f'tries left {attempts_count}, input your number -')
        if int(user_input) == num:
            return True
        elif int(user_input) < num:
            print('input higher')
        else:
            print('input lower')

# print(f'result = {find_num(1, 10, 10)}')
