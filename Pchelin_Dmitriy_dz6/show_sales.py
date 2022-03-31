from sys import argv
numbers = argv

with open('bakery.csv ', 'r', encoding='utf-8') as f:
    text = f.read().splitlines()
    begin = int(numbers[1])
    end = int(numbers[2])
    for i in range(begin-1,end):
        print(text[i])

