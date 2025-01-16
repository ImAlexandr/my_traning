# Задача "Некорректность":

class Car:
    # def __init__('Model1', 1000000, 'f123dj')):
    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.vin_number = __vin
        self.numbers = __numbers
        Car.__is_valid_vin(self)
        Car.__is_valid_numbers(self)

    def __is_valid_vin(self):  # - принимает vin_number и проверяет его на корректность. Возвращает (True,
        # если) корректный, в других случаях выбрасывает исключение. Уровень доступа private.
        if isinstance(self.vin_number, int):
            if self.vin_number >= 1000000 and self.vin_number <= 9999999:
                return True
            else:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            raise IncorrectVinNumber('Некорректный тип vin номер')

    def __is_valid_numbers(self):  # - принимает numbers и проверяет его на корректность. Возвращает (True,
        # если) корректный, в других случаях выбрасывает исключение. Уровень доступа private.
        if isinstance(self.numbers, str):
            if len(self.numbers) == 6:
                return True
            else:
                raise IncorrectCarNumbers('Неверная длина номера')
        else:
            raise IncorrectVinNumber('Некорректный тип данных для номеров')


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):  #
    def __init__(self, message):
        self.message = message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

"""
Вывод на консоль:
Model1 успешно создан
Неверный диапазон для vin номера
Неверная длина номера
"""
