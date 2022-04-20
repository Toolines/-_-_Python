class StockTech:
    firm = 'HP'

    def __init__(self,num):
        self.num = num

    def income(self, _income_num):
        self._income_num = _income_num
        try:
            self.num +=int(_income_num)
        except:
            print('Введенное число не распознано')

class Printer(StockTech):
    print_per_min = 60

class Scanner(StockTech):
    scan_per_min = 30

class Xerox(StockTech):
    xer_per_min = 15

pr, sc, xe = Printer(0), Scanner(0), Xerox(0)
a = ''
while a !='stop':
    a = input('Введите тип техники (принтер, сканер, ксерокс), для окончания ввода - введите команду stop ')
    if a != 'stop':
        num = input('Введите количество поступившей техники ')
        if a == 'принтер': pr.income(num)
        elif a == 'сканер': sc.income(num)
        elif a == 'ксерокс': xe.income(num)

print(f'На складе: {pr.num} принтеров')
print(f'На складе: {sc.num} сканеров')
print(f'На складе: {xe.num} ксероксов')