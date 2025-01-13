#   Задание "Программистам всё можно"

def add_everything_up(a, b):
    try:
        rez = round(a + b, 3)
    except TypeError:
        rez = str(f'{a}{b}')
    return rez


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
