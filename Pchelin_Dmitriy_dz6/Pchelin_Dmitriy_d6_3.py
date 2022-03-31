import csv
# создание файлов
users = [
    ['Иванов','Иван','Иванович'],
    ['Петров','Петр','Петрович'],
]
hobbys = [
    ['скалолазание','охота'],
    ['горные лыжи']
]

with open('users.csv', "w", encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(users)

with open('hobby.csv', "w", encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(hobbys)
# задание 3,4
file_users = open('users.csv', 'r', encoding='utf-8')
file_hobby = open('hobby.csv', 'r', encoding='utf-8')
user = file_users.read().splitlines()
hobby = file_hobby.read().splitlines()
result = {}
users = []
for i in range(0,len(user)):
    users.append(user[i].split(','))                # парсинг
    hobbys.append(hobby[i].split(','))
    result['{0} {1} {2}'.format(users[i][0], users[i][1], users[i][2])] = hobbys[i]
print(result)
file_users.close()
file_hobby.close()