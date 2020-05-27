# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

# my_dict = {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”}
# my_dict = {"название": 'сканер', "цена": 2000, "количество": 7, "eд": 'шт.'}
# my_tuple = [1, my_dict]
# print(my_tuple)

num = int(0)
materials = []
while input("Хотите добавить довар? д/н \n") == 'д':
    num += 1
    features = {}
    feature_key = "название"
    feature_value = input("Введите название товара: \n")
    features["название"] = feature_value
    feature_key = "цена"
    feature_value = input("Введите цену товара: \n")
    features["цена"] = feature_value
    feature_key = "количество"
    feature_value = input("Введите количество товара: \n")
    features["количество"] = feature_value
    feature_key = "ед"
    feature_value = input("Введите еденицы измерения товара: \n")
    features["ед"] = feature_value
    materials.append(tuple([num, features]))
    # analytics.update(
    #     {'название': features.get('название'),
    #      'цена': features.get('цена'),
    #      'количество': features.get('количество'),
    #      'ед': features.get('ед')
    #      }
    # )
print(materials)
# print(type(materials))
# print(analytics)
# for key, value in nums.items():
#     print(key, 'is', value)

# materials = [(1, {'название': 'компьютер', 'цена': '111'}), (2, {'название': 'мышь', 'цена': '42'})]
# materials = [(1, {'название': 'компьютер', 'цена': '111'}), (2, {'название': 'мышь', 'цена': '42'})]
# # t = materials.get("название")
# a = materials[0][1]
# b = a
# print(type(a))
# anal_table2 = anal_table.get("название")
# print(anal_table)
# # print(type(anal_table))
# print(anal_table2)
# # print(type(anal_table2))


product_template = {
    'название': ("имя товара"),
    'цена': ('стоимость товара'),
    'количество': ('кол-во товара'),
    'ед': ('кол-во товара'),
}
products_analytics = {}
for key in product_template:
    result = []
    for itm in materials:
        result.append(itm[1][key])
    products_analytics[key] = result
print(products_analytics)
# print(materials)
# print(type(materials))
# print(materials[0][1]['цена'])
# print(type(materials[0][1]))
