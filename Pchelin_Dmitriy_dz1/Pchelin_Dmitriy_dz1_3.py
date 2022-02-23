for i in range(1,101):                                      #цикл для перебора чисел от 1 до 100
    if (i%10 == 1) and not (i in range(10,20)):             #проверка окончаний чисел для выбора сколнения и вывод
        print(i, ' процент')
    elif (i%10 in range(2,5)) and not (i in range(10,20)):
        print(i, ' процента')
    else:
        print(i, ' процентов')