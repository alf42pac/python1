#Lesson 3_1

def _(a,b):
    try:
        a, b = int(a), int(b)
        x = a / b
    except ValueError:
        return "Ошибка!"
    except ZeroDivisionError:
        return "Запрещение деление на ноль!"
    return round(x, 4)

print(_(input("Введите первое число - "), input("Введите второе число -")))