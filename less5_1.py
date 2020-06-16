# Lesson5_1

with open('ltext_5-1.txt', 'w', encoding='utf-8') as alf:
    while True:
        a = input('Введите новую строку или пустую строку для завершения - ')
        if not a:
            break

        print(a, file=alf)
