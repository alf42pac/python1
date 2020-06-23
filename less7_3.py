# Lesson 7_3

class Cage:
    def __init__(self, a):
        self.a = a

    def order(self, line):
        return '\n'.join(['*' * line for i in range(self.a // line)]) + '\n' \
               + '*' * (self.a % line)

    def __str__(self):
        return self.a

    def __add__(self, other):
        return f'Сумма - {self.a + other.a}'

    def __sub__(self, other):
        return self.a - other.a if self.a - other.a > 0 else "Вычитание невозможно!"

    def __mul__(self, other):
        return f'Умножение - {self.a * other.a}'

    def __truediv__(self, other):
        return f'Деление - {round(self.a / other.a)}'


cage1 = Cage(33)
cage2 = Cage(44)
print(cage1 + cage2)
print(cage1 - cage2)
print(cage1 * cage2)
print(cage1 / cage2)
print(cage2.order(5))
