cubes = []                        #создание пустого списка
for i in range(1,1000,2):         #добаление кубов нечетных чисел от 1 до 1000
    cubes.append(i**3)
print(cubes)
task_a = 0                        #создание переменных для записи результатов заданий пунктов a,b,c
task_b_c = 0
for i in cubes:                   #цикл проходящий по всем элементам списка
    j = 10
    sum = i%10
    while (i//j) != 0:            #цикл для подсчета суммы цифр числа
        sum += i//j
        j = j*10
    if sum % 7 == 0:               #проверка кратности 7 суммы цифр
        task_a += sum              #подсчет итоговой суммы чисел при истинность условия
print(task_a)
for ind,item in enumerate(cubes):  #цикл для увеличения каждого числа списка на 17
    cubes[ind] = cubes[ind]+17
print(cubes)
for i in cubes:                    #тот же код как и к заданию пункта а, но для обновленного цикла
    j = 10
    sum = i%10
    while (i//j) != 0:
        sum += i//j
        j = j*10
    if sum % 7 == 0:
        task_b_c += sum
print(task_b_c)