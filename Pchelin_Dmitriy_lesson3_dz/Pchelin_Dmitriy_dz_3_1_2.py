def num_translate_adv(num):
    num_dict = {'one': 'один', 'two': 'два', 'three': 'три','four': 'четыре',
                'five': 'пять', 'six':'шесть', 'seven':'семь',
                'eight': 'восемь', 'nine':'девять', 'ten':'десять'}
    num_l = num.lower()
    if num_dict.get(num_l):     # проверка наличия ключа вне зависимости от заглавности
        if num.istitle():       # проверка на заглавие
            num_u = num_dict[num_l]
            print(num_u.title())
        else:
            print(num_dict[num_l])
    else: print('None')

num = input('Введите число на английском языке: ')
num_translate_adv(num)