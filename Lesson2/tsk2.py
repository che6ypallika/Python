# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
second_List = ['We dont need', 42, 3.14, None ,'Education']

id = 0
# while id < len(second_List):
while id < len(second_List[:-1]):
    second_List[id], second_List[id + 1] = second_List[id + 1], second_List[id]
    id += 2
print(second_List)

