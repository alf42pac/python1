#Lesson4_1

from sys import argv

def alf():
    try:
        t, a, b = map(int, argv[1:])
        print(f"Зарплата - {t * a + b}")
    except ValueError:
        print("Введите ВСЕ три числа. Не строку и не пустой символ!")


alf()