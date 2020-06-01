# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
def func_user (name, surname, bd, city, email, phone):
    return name + surname + bd + city + email + phone



result = func_user(name = 'Nikita', surname = 'Vladimirov',
                   bd = '11.03.1985', city = 'Msk',
                   email = 'test@tet.ru', phone = '588855554')

print(result)