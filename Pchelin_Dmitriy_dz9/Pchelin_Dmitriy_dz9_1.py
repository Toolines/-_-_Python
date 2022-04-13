import time

class TrafficLight:
    __color = ''

    def running(self):
        self.__color = 'Красный'
        print(self.__color)
        time.sleep(7)
        self.__color = 'Желтый'
        print(self.__color)
        time.sleep(2)
        self.__color = 'Зеленый'
        print(self.__color)
        time.sleep(7)

a = TrafficLight()
a.running()