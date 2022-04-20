class Own_err(Exception):
    def __init__(self,txt):
        self.txt = txt

user_list = []
a = ''
while a != 'stop':
    a = input('Введите число: (Для окончания ввода введите stop) ')
    try:
        b = int(a)
    except ValueError:
        if a != 'stop':
            err = Own_err('Вы ввели не число')
            print(err)
    else: user_list.append(b)

print(user_list)

