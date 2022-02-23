seconds = int(input('Введите количество секунд: '))         #ввод секунд
print(seconds, ' секунд это:')
minutes = seconds // 60             #подсчет количества минут
if minutes!=0:                      #запись остатка секунд после подсчета минут
    seconds = seconds % 60
hours = minutes // 60               #аналогично для часов
if hours!=0:
    minutes = minutes % 60
days = hours // 24                  #аналогично для дней
if days !=0:
    hours = hours % 24
if days != 0:                       #вывод результата в зависимости от величины подсчтанного времени
    print('Дней:',days,',часов:',hours,',минут:',minutes,',секунд:',seconds)
elif hours != 0:
    print('Часов:',hours, ',минут:', minutes, ',секунд:', seconds)
elif minutes != 0:
    print('Минут:', minutes, ',секунд:', seconds)
else :
    print('Секунд:', seconds)


