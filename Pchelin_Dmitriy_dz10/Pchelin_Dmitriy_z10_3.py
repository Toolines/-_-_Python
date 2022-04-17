class Cell:
    def __init__(self, arg):
        self.arg = arg

    def __add__(self, other):
        return Cell(self.arg + other.arg)

    def __sub__(self, other):
        if self.arg >= other.arg: return Cell(self.arg - other.arg)
        else: return Cell(f'Разность меньше нуля, операция не выполнима')

    def __mul__(self, other):
        return Cell(self.arg * other.arg)

    def __floordiv__(self, other):
        return Cell(self.arg // other.arg)

    def make_order(self, numbers):
        for _ in range(self.arg // numbers):
            print('*' * numbers , end='|')
        print('*' * (self.arg % numbers))

a = Cell(12)
b = Cell(15)
a.make_order(5)
b.make_order(5)

'''Операции:'''
print((a + b).arg)
print((a - b).arg)
print((b - a).arg)
print((a * b).arg)
print((a // b).arg)
print((b // a).arg)
