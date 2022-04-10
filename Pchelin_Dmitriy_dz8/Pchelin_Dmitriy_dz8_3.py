def type_logger(func):
    def wraper(num):
        print(f'{func.__name__} ({num}: {type(num)})')
        return func(num)

    return wraper

@type_logger
def calc_cube(a):
    return a ** 3

a = calc_cube(5)
print(a)


