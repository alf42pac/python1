# Lesson 8_7

class Complex():
    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im

    def __add__(self, other):
        return (Complex(self.Re + other.Re, self.Im + other.Im))

    def __sub__(self, other):
        return (Complex(self.Re - other.Re, self.Im - other.Im))

    def __mul__(self, other):
        return (Complex(self.Re * other.Re - self.Im * other.Im, self.Re * other.Im + self.Im * other.Re))

    def comlexprint(self, name):
        print(name, ' = ', self.Re, ' + ', self.Im, 'i')


a = Complex(1, 5)
b = Complex(-3, -1)
a.comlexprint('a')
b.comlexprint('b')
c = a + b
c.comlexprint('a + b')
c = a * b
c.comlexprint('a * b')
c = a - b
c.comlexprint('a - b')
c = b * a
c.comlexprint('b * a')
