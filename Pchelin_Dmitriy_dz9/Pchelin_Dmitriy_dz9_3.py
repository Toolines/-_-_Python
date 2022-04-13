class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name, self.surname, self.position = name, surname, position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')

    def get_total_icome(self):
        print(f'Доход с учетом премии: {sum(self._income.values())}')

Person = Position('Иван', 'Иванов', 'Учитель', 1000, 500)
Person.get_full_name()
Person.get_total_icome()