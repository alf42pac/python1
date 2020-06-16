# Lesson5_2

with open("ltext_5-2.txt", encoding='utf-8') as a:
    line = a.readlines()
    for i, j in enumerate(line, 1):
        x = len(j.split())
        print(f'Строка {i} содержит {x} слов')
