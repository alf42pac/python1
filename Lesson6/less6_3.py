#Lesson6_3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage" : wage, "bonus" : bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name(self):
        return (self.name + " " + self.surname)
    def total_income(self):
        return (self._income["wage"] + self._income["bonus"])


ex1 = Position('Ramzan', 'Sechin', 'big boss', 21, 1)
ex2 = Position('Vladimir', 'Kirkorov', 'lil boss', 15, 2)
b = ex1.get_full_name()
c = ex1.total_income()
print('Name worker: ' + b)
print('Total income: ' , c)
b = ex2.get_full_name()
c = ex2.total_income()
print('Name worker: ' + b)
print('Total income: ' , c)
