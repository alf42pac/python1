#Lesson4_5

from functools import reduce

def alf(a, b):
    return a * b

x = [i for i in range(1, 99, 2)]
print(f"Список\n{x}\nПеремножение чисел\n{reduce(alf, x)}")