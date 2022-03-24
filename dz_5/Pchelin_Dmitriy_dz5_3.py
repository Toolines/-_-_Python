tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

while len(klasses)<=len(tutors):     # добавление элементов None при меньшем размере ссписка klasses
    klasses.append('None')

res_gen = ((tutors[i], klasses[i]) for i in range(0, len(tutors)))
print(*res_gen)
