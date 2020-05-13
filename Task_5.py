while True:
    revenue = input('Введите выручку\n')
    if revenue.isdigit():
        revenue = int(revenue)
        break
    else:
        print('Введите ЧИСЛО в качестве выручки! ')

while True:
    cost = input('Введите затраты\n')
    if cost.isdigit():
        cost = int(cost)
        break
    else:
        print('Введите ЧИСЛО в качестве выручки! ')

if revenue > cost:
    print('Умудряетесь работать в прибыль? \nЗаявка на проверку подана в налоговую! ')
    profit = (revenue / cost - 1) * 100
    print("Ваша рентабильность %.1f" %  profit, '%' )
    while True:
        staff = input('Укажите количество сотрудников\n')
        if staff.isdigit():
            staff = int(staff)
            break
        else:
            print('Введите ЧИСЛО сотрудников! ')
    print(f"Прибыль на сотрудника : {((revenue - cost) / staff):.1f}")

elif revenue < cost:
    print('Прибыли нет, но вы держитесь!')
else:
    print('Рговненько идете, товаРгищи')