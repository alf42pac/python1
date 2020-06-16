# Lesson5_5

from random import randint

x = 0
with open("ltext_5-5.txt", "w", encoding="utf-8") as alf:
    for i in range(50):
        a = randint(1, 100)
        x += a
        alf.write(str(a) + " ")

print(f"Сумма элементов - {x}")
