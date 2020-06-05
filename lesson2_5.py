#lesson2_5

_list = [9, 9, 8, 8, 7, 7, 7, 6, 5, 5, 4, 3, 2, 2, 2, 1]
numb = int(input("Введите новый элемент - "))
i = 0
for n in _list:
    if numb <= n:
        i += 1
_list.insert(i, float(numb))
print(_list)