#Lesson 3_4

def _(a, b):
    try:
        a, b = float(a), int(b)
        if a<= 0 or b >= 0:
            return 'Неверно введено одно из чисел! Читайте внимательно условие ввода!'
        else:
            res = 1
            for _ in range(abs(b)):
                res *= 1 / a
            return f'Результат возведения в степень - {round(res, 6)}'
    except ValueError:
        return "Введите число! Пожалуйста, внимательно читайте условия ввода!"

print(_(input('Введите действительное положительное число, a = '),input('Введите целое отрицательное число, b = ')))
