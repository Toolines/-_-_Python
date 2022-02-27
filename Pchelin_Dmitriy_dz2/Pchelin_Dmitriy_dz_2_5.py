prices = [50.8, 10.5, 21.9, 11.8, 45.16, 99, 104.3, 21.2, 14.4]

def task(prices):
    rub = 0
    cop = 0
    cents = ''
    for i in prices:
        rub = int(i)
        cop = round(i%1,2)
        if (cop*10)%1==0:
           cents = '0'+str(round(cop*10))
        else:
           cents = str(round(cop*100))
        print(f'{rub} рублей {cents} копеек,', end=' ')
    print()

task(prices)
prices.sort()
task(prices)
prices.sort(reverse=True)
task(prices)