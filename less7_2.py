# Lesson 7_2

from abc import ABC, abstractmethod


class Dress(ABC):
    def __init__(self, a):
        self.a = a

    @abstractmethod
    def expenditure(self):
        pass


class TopCoat(Dress):
    @property
    def expenditure(self):
        return f'Расход ткани на пошив пальто - {round(self.a / 5.5) + 1.5}\n'


class Suit(Dress):
    @property
    def expenditure(self):
        return f'Расход ткани на пошив костюма - {self.a * 2.5 + 0.7}\n'


topcoat = TopCoat(33)
suit = Suit(123)
print(topcoat.expenditure + suit.expenditure)
