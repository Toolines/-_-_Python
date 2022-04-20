class Complex_num:
    def __init__(self, real, imagine):
        self.real = real
        self.imagine = imagine

    def __str__(self):
        return f'{self.real}+{self.imagine}i'

    def __add__(self, other):
        return Complex_num(self.real + other.real, self.imagine + other.imagine)

    def __mul__(self, other):
        a1, b1, a2, b2 = self.real, self.imagine, other.real, other.imagine
        return Complex_num((a1 * a2 - b1 * b2), a1 * b2 + a2 * b1)


a, b = Complex_num(1, 2), Complex_num(3, 4)
print(a)
print(b)
c = a + b
d = a * b
print(f'{a} + {b} = {c}')
print(f'{a} * {b} = {d}')
