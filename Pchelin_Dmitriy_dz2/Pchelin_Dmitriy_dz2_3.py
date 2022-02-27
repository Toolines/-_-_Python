task_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+', '5', 'градусов']

for ind,item in enumerate(task_list):              #цикл для прохода по элементам
    if item.isdigit() and task_list[ind-1] != '"': #проверка чисел в элементах и флажка " чтобы небыло зацикливания
        if int(item) // 10 == 0:                   # проверка и добавление 0 при 1 разряде числа
            task_list[ind] = '0'+ item
        task_list.insert(ind+1, '"')                #добавление ковычек
        task_list.insert(ind,'"')
print(task_list)
print(" ".join(task_list))


