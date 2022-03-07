from requests import get, utils

def currency_rates(money):
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
    return date, cor_curs

money = input('Введите код интересующей вас валюты: ')
money = money.upper()                   # Перевод введенной валюты в верхний реестр
result = currency_rates(money)

print(f'Курс валюты: ', money, ' на ',result[0], ' по отношению к рублю: ', result[1])

