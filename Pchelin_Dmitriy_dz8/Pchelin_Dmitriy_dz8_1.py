import re

def email_parse(email):
    regex = re.compile(r'[\w\.]+@[\w]+\.[\w\.]+')
    is_match = regex.match(email)
    if is_match:
        return dict(zip(['user','domian'], is_match.group().split('@')))
    raise ValueError(f'Адрес: {email} - неверный')

if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    print(email_parse('someone@geekbrainsru'))

