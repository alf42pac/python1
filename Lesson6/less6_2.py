#Lesson6_2

class Road:

    def __init__(self, val1, val2):
        self._length = val1
        self._width = val2

    def count(self):
        print(self._length * self._width * 25 * 5)


a = Road(10, 10)
a.count()
