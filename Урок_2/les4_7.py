#Lesson4_7

from itertools import count
from math import factorial

def alf():
    for i in count(1):
        yield factorial(i)

x = alf()
y = 0
for i in x:
    if y == 20:
        break
    else:
        y += 1
        print(f"Факториал {y} = {i}")
