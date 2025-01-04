# Задача "История строительства":

class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        print(f'{cls.houses_history}')
        return object.__new__(cls)

    def __init__(self, *args):
        self.name = args[0]
        self.number_of_floors = args[1]

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


# Регистрация объектов
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h3 = House('ЖК Матрёшки', 20)

# Удаление объектов
del h2
del h3

# Список "История строительства"
print(House.houses_history)
