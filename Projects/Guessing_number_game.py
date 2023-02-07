from random import *


def is_valid(n, x, y):
    return n.isdigit() and x <= int(n) <= y


def input_num(min_n=0, max_n=9 ** 30):
    while True:
        user_num = input()
        if is_valid(user_num, min_n, max_n):
            return int(user_num)
        else:
            print(f'А может быть все-таки введем целое число от {min_n} до {max_n}?')


def compare_num(min_n, max_n):
    num = randint(min_n, max_n)
    total = 0
    while True:
        n = input_num(min_n, max_n)
        total += 1
        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще раз')
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще раз')
        else:
            print(f'Ура! Вы угадали ответ за {total}, поздравляем!')
            break


def continue_game():
    ans = input('Начать новую игру ("д"/"н"/"y"/"n")?\n')
    while True:
        if ans not in ('y', 'д', 'n', 'н'):
            ans = input('Введите корректную букву("д"/"н"/"y"/"n")!!!\n')
        elif ans in ('n', 'н'):
            print('До новых встреч!')
            return False
        else:
            return True


def game():
    print('Добро пожаловать в игру "Угадайка чисел"')
    while True:
        print('Укажите диапозон загаданного числа')
        print('Введите начальную границу диапозона:')
        x = input_num()
        print('Введите конечную границу диапозона:')
        y = input_num()
        if x > y:
            x, y = y, x
        print('Введите число от', x, 'до', y)
        compare_num(x, y)
        if continue_game():
            continue
        else:
            break


game()
