#Lesson4_4

from random import randint

alf = [randint (-5, 5) for i in range(20)]
a = [i for i in alf if alf.count(i) == 1]
print(f"Список\n{alf}\nБез повторений\n{a}")