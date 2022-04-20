from datetime import date
class Data:

    def __init__(self,str_data):
        self.str_data = str_data

    @classmethod
    def num_data(cls, str_data):
        return [int (x) for x in str_data.split('-')]

    @staticmethod
    def valid_data(data):
        list = [int (x) for x in data.split('-')]
        if (list[0] in range(0,10000)) and (list[1] in range(1, 13)) and (list[2] in range(1,30)):
            return 'Дата верна'
        else: return 'Дата неверна'

print(Data.num_data(str(date.today())))
print(Data.valid_data(str(date.today())))
print(Data.valid_data('2022-00-14'))

