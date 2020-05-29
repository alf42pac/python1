num = input('Введите целое положительное число: ')
i = 0
max_num = int(num[0])
while( i < len(num)):
    if(int(num[i]) > max_num):
        max_num = int(num[i])
    i = i + 1
print('Самая большая цифра в числе: ', max_num)
