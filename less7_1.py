# Lesson 7_1

matr1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
matr2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


class Matr:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return '\n'.join(map(str, self.a))

    def __add__(self, other):
        b = []
        for i in range(len(self.a)):
            b.append([])
            for j in range(len(self.a[0])):
                b[i].append(self.a[i][j] + other.a[i][j])
        return '\n'.join(map(str, b))


print(f"Матрица 1\n{Matr(matr1)}\n{'-' * 20}")
print(f"Матрица 2\n{Matr(matr2)}\n{'-' * 20}")
print(f"Сумма \n{Matr(matr1) + Matr(matr2)}")
