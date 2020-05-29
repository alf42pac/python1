sec = float(input('Пожалуйста, введите время в секундах: '))
hour = sec // 3600
sec -= 3600*hour
minuts = sec // 60
sec -= 60*minuts
print("%d:%d:%f" %(hour, minuts, sec))

