while True:
    num = input('Введите число\n')
    if num.isdigit():
        num = int(num)
        break
    else:
        print('ЧИСЛО! а не что-то другое')

num2 = int(str(num) * 2)
num3 = int(str(num) * 3)

print(num + num2 + num3)