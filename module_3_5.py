# Задача "Рекурсивное умножение цифр":

def get_multiplied_digits(number: int):  # и подсчитывает произведение цифр этого числа.

    str_number = str(number).replace('0', '')
    if number < 0:
        k = -1
        str_number = str(number).replace('-', '')
    elif number == 0:
        return (0)
    else:
        k = 1

    first = int(str_number[0])

    if len(str_number) > 1:
        multiply = first * get_multiplied_digits(int(str_number[1:]))
    else:
        multiply = first
    return (multiply * k)


result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(402030)
print(result2)

result3 = get_multiplied_digits(0000000)
print(result3)

result4 = get_multiplied_digits(10)
print(result4)

result5 = get_multiplied_digits(-205)
print(result5)
