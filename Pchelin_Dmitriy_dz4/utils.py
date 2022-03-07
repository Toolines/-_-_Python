from requests import get, utils

def currency_rates(money):
    money = money.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    econdings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=econdings)
    curses = content.split('ID')        #Разбиение валют по разделителю ID
    for i in curses:
        if money in i:
            curs = i                    # сохранение строки с нужной валютой
    # print(curs)
    rate = curs.find('Value')
    curs = curs[(rate+6):]           # стрез от строки cо значение курса
    num = ''
    for i in curs:                      # поиск значения курса в строке
        if i.isdigit() or i ==',':
            num = num + i
    num = num.replace(',','.')          # замена , на . для перевода в тип float

    cor_curs = float(num)
    s = content.find('ValCurs Date=')   # поиск даты
    date = content[(s+14):(s+24)]
    print(f'Курс валюты: ', money, ' на ', date, ' по отношению к рублю: ', cor_curs)
    return 0

if __name__ == '__main__':
    import sys
    print(sys.argv)
    money = sys.argv[1]
    currency_rates(money)