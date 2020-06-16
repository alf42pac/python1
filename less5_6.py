# Lesson5_6

alf = {}
with open("ltext_5-6.txt", encoding="utf-8") as alf_obj:
    for i in alf_obj:
        a, b = i.split(':')
        x = sum(map(int, "".join([j for j in b if j == ' ' or (j >= '0' and j <= '9')]).split()))
        alf[a] = x

print(f"{alf}")
