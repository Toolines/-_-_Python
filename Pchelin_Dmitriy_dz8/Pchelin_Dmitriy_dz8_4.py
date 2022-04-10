from functools import wraps

def val_checker(l_func):
    def _val_checker(func):
        @wraps(func)
        def wrapper(num):
            if l_func(num):
                res = func(num)
            else:
                raise ValueError(f'неверное значение: {num}')
            return res
        return wrapper
    return _val_checker

@val_checker( lambda x: x > 0)
def cal_cube(a):
    return a ** 3

print(cal_cube(-5))