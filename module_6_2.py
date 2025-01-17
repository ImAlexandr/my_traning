#  Задача "Изменять нельзя получать"
#  Цели: Применить сокрытие атрибутов и повторить наследование

class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str, __model: str, __color: str, __engine_power: int):
        self.owner = owner  # - владелец транспорта. (владелец может меняться)
        self.__model = __model  # - модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = __engine_power  # - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        self.__color = __color  # - название цвета. (мы не можем менять цвет автомобиля своими руками)

    def get_model(self):  # - возвращает строку: "Модель: <название модели транспорта>"
        return f'Модель: {self.__model}'

    def get_horsepower(self):  # - возвращает строку: "Мощность двигателя: <мощность>"
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):  # - возвращает строку: "Цвет: <цвет транспорта>"
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(vehicle1.get_model())
        print(vehicle1.get_horsepower())
        print(vehicle1.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str):
        for color in self.__COLOR_VARIANTS:
            if new_color.lower() == color.lower():
                self.__color = new_color
                return
        print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    # __PASSENGERS_LIMIT = 5
    def __init__(self, owner, __model, __color, __engine_power):
        Vehicle.__init__(self, owner, __model, __color, __engine_power)
        self.__PASSENGERS_LIMIT = 5
        print(f'В седан может поместиться только {self.__PASSENGERS_LIMIT} пассажиров')
        print()


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

"""
Вывод на консоль:
Модель: Toyota Mark II
Мощность двигателя: 500
Цвет: blue
Владелец: Fedos
Нельзя сменить цвет на Pink
Модель: Toyota Mark II
Мощность двигателя: 500
Цвет: BLACK
Владелец: Vasyok
"""
