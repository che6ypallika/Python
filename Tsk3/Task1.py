# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

while True:
    a = input('Введите чило a \n')
    if a.isdigit():
        a = int(a)
        break
    else:
        print('Введите ЧИСЛО! ')

while True:
    b = input('Введите чило b \n')
    if b.isdigit():
        b = int(b)
        if int(b) == 0:
            print('На нуль делить нельзя! Введите другое число ')
            continue
        break
    else:
        print('Введите ЧИСЛОб не текст! ')

def first_func(c, d) -> int:
    return c / d

print(first_func(a, b))
