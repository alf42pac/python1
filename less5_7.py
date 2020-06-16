#Lesson5_7

import json

x = []
with open("ltext_5-7_new.txt", "w", encoding="utf-8") as a:
    with open("ltext_5-7.txt", encoding="utf-8") as b:
        y = {}
        for i in b:
            y[i.split(' ')[0]] = int(i.split(' ')[2]) - int(i.split(' ')[3])
        z = sum([int(j) for j in y.values() if int(j) > 0]) / len([int(j) for j in y.values() if int(j) > 0])
        x.append(y)
        x.append({"Средняя_прибыль": round(z)})
    json.dump(x, a)
