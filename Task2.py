while True:
    time_sec = input('Введите количество секунд\n')
    if time_sec.isdigit():
        time_sec = int(time_sec)
        break
    else:
        print('Введите число секунд')

hours = time_sec / 3600
minutes = (time_sec % 3600) / 60
seconds = (time_sec % 3600) % 60

print("%.2d:%.2d:%.2d" % (hours,minutes,seconds))