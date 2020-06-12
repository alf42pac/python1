#lesson2_4

_str = input('Enter the numbers with space - ').split()

for i, n in enumerate(_str, 1):
    print(f'{i} {n[:10]}')