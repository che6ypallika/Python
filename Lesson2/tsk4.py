# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
Usr_inp = input('Введитебилеберду через пробел\n')
By_word = Usr_inp.split(' ')
print(list(enumerate(By_word)))
# print(enumerate(By_word))
print(By_word[1])

for ind, el in enumerate(By_word):
    print(f'{ind}:{el[:10]}')
