# Задача Задача "Магические здания":

class House:
    def __init__(self, name: str, floor: int):
        self.name = name
        self.number_of_floors = floor

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __len__(self):
        floors = []
        for i in range(1,self.number_of_floors+1):
            floors.append(i)
        return len(floors)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
