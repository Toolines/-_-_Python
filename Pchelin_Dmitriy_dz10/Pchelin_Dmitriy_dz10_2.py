from abc import ABC, abstractmethod

class Clothes:
    def __init__(self, arg):
        self.arg = arg

    @abstractmethod
    def calculation(self):
        pass

class Coat(Clothes):
    @property
    def calculation(self):
        return self.arg / 6.5 + 0.5

class Suit(Clothes):
    @property
    def calculation(self):
        return self.arg * 2 + 0.3

coat1 = Coat(48)
suit1 = Suit(1.72)
print(f'Суммарный расход ткани для пальто: {coat1.calculation}')
print(f'Суммарный расход ткани для костюма: {suit1.calculation}')