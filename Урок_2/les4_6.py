#Lesson4_6

from itertools import islice, cycle, count

def alf(a, b, c):
    try:
        a, b, c = int(a), int(b), int(c)
        x = [i for i in islice(count(), a, b + 1)]
        y = iter(i for i in cycle(x))
        z = [next(y) for _ in range(c)]
        print(x)
        return z
    except ValueError:
        return "Ошибка значения!"
    except TypeError:
        return "Ошибка ввода!"

print(alf(input("Список начинается с - "), input("до - "), input("Количество повторений - ")))

