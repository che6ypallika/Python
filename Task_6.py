while True:
    distance_a = input('Введите начальное количество километров\n')
    if distance_a.isdigit():
        distance_a = int(distance_a)
        break
    else:
        print('Введите ЧИСЛО в качестве километров! ')

while True:
    distance_b = input('Введите целевое количество километров\n')
    if distance_b.isdigit():
        distance_b = int(distance_b)
        break
    else:
        print('Введите ЧИСЛО в качестве километров! ')

day_end = 1
while distance_a < distance_b:
    distance_a = distance_a * 1.1
    day_end = day_end + 1
print("На", day_end,"-й день спортсмен достиг результата — не менее",distance_b, "км")

