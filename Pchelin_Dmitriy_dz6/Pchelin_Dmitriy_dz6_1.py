file = open('nginx_logs.txt', 'r', encoding='utf-8')        # чтение файла
text = file.read()
lines = text.splitlines()
# задание 1
result1 = []
for i in range(0,len(lines)):
    line = lines[i].split()
    result1.append((line[0], line[5].lstrip('"'), line[6]))
print(result1[0])                                            # проверка одного из элементов
# задание 2
result2 = {}
for i in range(0, len(result1)):              # создание словаря где ключи - адреса, значения - количество запросов
    if result1[i][0] in result2:
        result2[result1[i][0]] += 1
    else: result2[result1[i][0]] = 1

max_val = max(result2.values())                                 # поиск максимального значения из словаря
final_dict = {k: v for k, v in result2.items() if v == max_val}
print(final_dict)

file.close()