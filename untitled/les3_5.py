#Lesson 3_5

def _sum ():
    sum = 0
    while True:
        _ = input("Введите число или E для выхода: ").split()
        for n in _:
            if n == "E":
                return sum
            else:
                try:
                    sum += int(n)
                except ValueError:
                    print("Для выхода из программы нажмите E - ")
        print(f"Сумма чисел = {sum}")


print(_sum())