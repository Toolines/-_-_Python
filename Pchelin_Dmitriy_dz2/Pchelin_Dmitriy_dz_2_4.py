list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
names =[]

for i in list:
    names.append( i.split()[-1].capitalize())

print(names)
for i in names:
    print(f'Привет, {i}')