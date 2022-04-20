class DevZero(Exception):
    def __init__(self,txt):
        self.txt = txt

a , b = input('Введите делимое: '), input('Введите делитель: ')
try:
    a = int(a)
    b = int(b)
    res = a / b
except ValueError:
    print('Вы ввели не число')
except ZeroDivisionError:
    err = DevZero('Делитель равен нулю')
    print(err)
else: print(f'Частное от деления: {res}')