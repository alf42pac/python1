#lesson2.3

_month = input('Введите месяц (от 1 до 12) - ')
while True:
    if _month.isdigit() and 0 <= int(_month) <= 12:
        s_1 = ['Зима', 'Весна', 'Лето', 'Осень', 'Зима']
        s_2 = {0: 'Зима', 1: 'Весна', 2: 'Лето', 3: 'Осень', 4: 'Зима'}
        print(f'Список сезонов - {s_1[int(_month) // 3]}') \nСловарь сезонов - {s_2[int(_month) // 3]}
        break
    else:
        print("Ошибка")
        break
