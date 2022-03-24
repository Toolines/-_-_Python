# создание генератора с yield
def num_gen (n):
    for num in range(1, n+1, 2):
        yield num

n = int(input('Задайте число '))
odd_num = (num_gen(n))
print(*odd_num)

# создание генератора без yield

n = int(input('Задайте число '))
num_gens = (num for num in range(1, n+1, 2))
print(*num_gens)