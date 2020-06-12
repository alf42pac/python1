# Lesson#2.2

_list = input('Введите элементы массива (не забудьте разделить их пробелами) - ').split()
i=0
print(f'Список {_list}')
while i + 1 < len(_list):
    if i % 2 == 0:
        _list.insert(i, _list.pop(i+1))
    i += 1

print(f'Магический список {_list}')
