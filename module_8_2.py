# Задача "План перехват":

def personal_sum(numbers):
    result, incorrect_data = 0,0
    decision = ()
    if isinstance(numbers,str) or isinstance(numbers, list):
        for elm in numbers:     # Подсчитывать сумму чисел в numbers путём перебора
            try:
                result += elm   # и увеличивать переменную result.

            except TypeError:   # Если же при переборе встречается данное типа отличного от числового,
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы: {elm}')
            finally:
                decision = (result, incorrect_data) # кортеж из двух значений: result - сумма чисел, incorrect_data -
                                                    # кол-во некорректных данных.
    return decision

def calculate_average(numbers):
    decision = 0
    average = None
    try:
        if len(numbers) == 0:
            average = None
            print('В numbers записан некорректный тип данных')
            return average
        decision = personal_sum(numbers)
        average = decision[0]/(len(numbers)-decision[1])    #  сумма всех данных делённая на их количество.

    except ZeroDivisionError:
        # то обработайте исключение ZeroDivisionError при делении на 0 и верните 0.
        average = 0

    except TypeError:
        average = None
        print('В numbers записан некорректный тип данных')
    # может быть записана не коллекция, а другие типы данных, например числа. Обработайте исключение TypeError
    # выводя строку 'В numbers записан некорректный тип данных'. В таком случае функция просто вернёт None.
    finally:
        return average


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
print(f'Результат 5: {calculate_average([])}') # None
print(f'Результат 6: {calculate_average({})}') # None


"""
Вывод на консоль:
Некорректный тип данных для подсчёта суммы - 1
Некорректный тип данных для подсчёта суммы - ,
Некорректный тип данных для подсчёта суммы -
Некорректный тип данных для подсчёта суммы - 2
Некорректный тип данных для подсчёта суммы - ,
Некорректный тип данных для подсчёта суммы -
Некорректный тип данных для подсчёта суммы - 3
Результат 1: 0
Некорректный тип данных для подсчёта суммы - Строка
Некорректный тип данных для подсчёта суммы - Ещё Строка
Результат 2: 2.0
В numbers записан некорректный тип данных
Результат 3: None
Результат 4: 26.5"""


