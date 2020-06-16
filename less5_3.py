# Lesson5_3

with open("ltext_5-3.txt", "r", encoding="utf-8") as alf:
    x = []
    y = []
    a = alf.read().split("\n")
    for i in a:
        i = i.split()
        if float(i[1]) < 20000:
            y.append(i[0])
        x.append(i[1])

print(f"Зарплата менее 20.000 {y} \n Средний доход - {sum(map(float, x)) / len(x)}")
