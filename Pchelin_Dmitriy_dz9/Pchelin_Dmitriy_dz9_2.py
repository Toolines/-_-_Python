class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._width, self._length = width, length

    def asfault(self):
        return self._width*self._length*25*5/1000

mass = Road(5000,20)
print(mass.asfault())