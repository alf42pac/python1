#lesson2_6

goods = []
func = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
analyt = {'name': [], 'price': [], 'quantity': [], 'unit': []}
n = 0
while True:
    if input ('For exit press E, for continue Enter - ').upper() == 'E':
        break
    n += 1
    for i in func.keys():
        _ = input(f'Enter properties "{i}": ')
        func[i] = int(_) if (i == 'price' or i == 'quantity') else _
        analyt[i].append(func[i])
    goods.append((n, func))
    print(f'\n Current product analytics: \n {"*" * 30}')
    for key, value in analyt.items():
        print(f'{key[:25]:>30}: {value}')
    print("*" * 30)