# 4. Программа принимает
# действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись
# без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.
def func_user(a, b):
    return a ** b

print(func_user(2, -3))

# t = 5
# r = 3
# temp_i = 0
# while temp_i  <= r:
#     c = t * t
#     temp_i = temp_i + 1
# print (c)


def my_mult(x, y):
    result = 0
    for el in range(y):
        result += x
    return result
# print(my_multip(5,3))


def func_user2(x, y):
    result = 1
    for el in range(abs(y)):
        result = my_mult(result, x)
    return result if y > 0 else 1 / result


print(func_user2(5,-3))



