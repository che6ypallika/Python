 # Пользователь вводит месяц в виде целого числа от 1 до 12.
 # Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
 # Напишите решения через list и через dict.

Month_inp = int(input('Введитен номер месяца\n'))
if  0 < Month_inp < 13:
    Month_inp = int(Month_inp)
else:
     print('Введитен номер месяца\n')

month_lst = [1, "Зима", 2, "Зима" ,12, "Зима", 3, "Весна", 4, "Весна", 5, "Весна", 6, "Лето", 7, "Лето", 8, "Лето", 9, "Осень", 10, "Осень", 11, "Осень"]
temp_el = month_lst.index(Month_inp)

print(month_lst[temp_el + 1])

month_dict = dict(key_1='Зима', key_2='Зима', key_3='Весна', key_4='Весна', key_5='Весна', key_6='Лето', key_7='Лето',
                  key_8='Лето', key_9='Осень',key_10='Осень', key_11='Осень', key_12='Зима')
# key_name = str("key_" + str(Month_inp))
# print(month_dict.get(key_name))
# print(key_name)
print(month_dict.get(str("key_" + str(Month_inp))))
# print(month_dict.get('key'+'2')
# my_dict = {"key_1": 500, 2: 400, "key_3": True, 4: None}
# print(my_dict)
