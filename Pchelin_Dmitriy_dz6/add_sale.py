from sys import argv
sale = argv
with open('bakery.csv ', 'a', encoding='utf-8') as f:
    f.write(sale[1]+ '\n')
