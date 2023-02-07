from random import *


def generate_pw(length, chars):
    pw = ''
    for i in range(length):
        pw += choice(chars)
    return pw


DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'

chars = ''

n = int(input('Укажите количество паролей для генерации:'))
length = int(input('Укажите длину одного пароля:'))
dig_on = input('Включать ли цифры 0123456789? (y/n)\n')
up_on = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)\n')
low_on = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)\n')
ch_on = input('Включать ли символы !#$%&*+-=?@^_? (y/n)\n')
exc_on = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)\n')
if dig_on.lower() == 'y':
    chars += DIGITS
if up_on.lower() == 'y':
    chars += LOWERCASE_LETTERS
if low_on.lower() == 'y':
    chars += UPPERCASE_LETTERS
if ch_on.lower() == 'y':
    chars += PUNCTUATION
if exc_on.lower() == 'y':
    for c in 'il1Lo0O':
        chars.replace(c, '')
for _ in range(n):
    print(generate_pw(length, chars))
