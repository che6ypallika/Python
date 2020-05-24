# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

First_list = ['We dont need', 42, 3.14, None ,'Education']
# print(type(First_list))
#
# print(len(First_list))
# print(First_list[1])
# End = len(First_list)
s = 0
while s < len(First_list):
    print(type(First_list[s]))
    s = s + 1
