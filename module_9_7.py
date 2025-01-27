# Задание: Декораторы в Python

def is_prime(func):
    def wrapper(*args):
        summ = func(*args)
        if summ == 2 or summ == 3:
            print("Простое")
        elif summ > 3:
            for i in range(2, summ - 1):
                if summ % i == 0:
                    print("Составное")
                    return summ
            print("Простое")
        else:
            print(f'Сумма чисел равна {summ}, и это ни "Простое" ни "Составное" число')
        return summ

    return wrapper


@is_prime
def sum_three(*args):
    summ = 0
    for i in args:
        summ += i
    return summ


result = sum_three(2, 3, 6)
print(result)

"""
Результат консоли:

Простое
11
"""
