class Stationery:
    title = ''
    def draw(self):
        print('Запуск отрисовки')

class Pen (Stationery):
    title = 'ручкой'
    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pencil (Stationery):
    title = 'карандашом'
    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Handle  (Stationery):
    title = 'маркером'
    def draw(self):
        print(f'Запуск отрисовки {self.title}')

a, b , c = Pen(), Pencil(), Handle()
a.draw(), b.draw(), c.draw()