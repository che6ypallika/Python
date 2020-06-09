def sum(items):
    resul = 0
    for itm in items:
        resul += itm
    return resul
# a = sum ([1, 4, 5 ,6])
# print(a)

def r_sum(items):
    return items[0] + r_sum(items[1:]) if items else 0


