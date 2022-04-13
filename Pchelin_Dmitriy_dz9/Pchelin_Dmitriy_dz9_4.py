class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police
    def go(self):
        print(f'{self.color} {self.name} поехала')
    def stop(self):
        print(f'{self.color} {self.name} остановилась')
    def turn(self, direction):
        self.direction = direction
        print(f'{self.color} {self.name} повернула на{self.direction}')
    def show_speed(self):
        print(f'Скорость {self.color} {self.name} = {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed,color,name)
    def show_speed(self):
        print(f'Скорость {self.color} {self.name} = {self.speed}') if self.speed <= 60 else print('Превышена допустимая скорость')

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed,color,name)

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed,color,name)
    def show_speed(self):
        print(f'Скорость {self.color} {self.name} = {self.speed}') if self.speed <= 40 else print('Превышена допустимая скорость')

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed,color,name, True)

a,b,c,d,e = Car(50, 'Черная', 'Toyota'), TownCar(68, 'Белая', 'Audi'), SportCar(50, 'Красная', 'Ferrri'),\
            WorkCar(30, 'Желтый', 'Трактор'), PoliceCar(40, 'Белый', 'УАЗик')
a.go(), a.stop(), a.turn('право'), a.show_speed()
b.go(), b.stop(), b.turn('право'), b.show_speed()