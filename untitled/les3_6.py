#Lesson 3_6

def _f (x):
    a, b = [], []
    if len(x) > 0:
        for _ in x.split():
            a.append(_[0].upper() + _[1:])
        b = ' '.join(a)
    return b

print(_f(input("Введите строку: ")))