while True:
    num = input('Введите число\n')
    if num.isdigit():
        num = int(num)
        break
    else:
        print('ЧИСЛО! а не что-то другое')

num_max = 0 # будем с этим сравнивать

while num > 0:
    if num%10 > num_max:
        num_max = num % 10
    num //= 10
print(num_max)