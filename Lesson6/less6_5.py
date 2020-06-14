#Lesson6_5

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')

s = Stationery('Stationery')
p = Pen('Pen')
pl = Pencil('Pencil')
h = Handle('Handle')

s.draw()
p.draw()
pl.draw()
h.draw()
