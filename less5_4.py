# Lesson5_4

alf = {"One": "Раз", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("ltext_5-4new.txt", "a") as alf_new:
    with open("ltext_5-4.txt") as alf_my:
        a = alf_my.read().split("\n")
        for i in a:
            i = i.split(" - ")
            alf_new.writelines(alf[i[0]] + ' - ' + i[1] + "\n")
