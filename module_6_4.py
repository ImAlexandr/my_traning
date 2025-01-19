# Задание "Они все так похожи":
import math

class Figure:
    sides_count = 0
    def __init__(self, *args, filled = False):
        self.filled = filled
        self.__color = list(args[0])
        sides = list(args[1:])
        if len(sides) == self.sides_count:
            self.__sides = sides
        else:
            self.__sides = [1]*self.sides_count
        if self.sides_count == 12 and len(sides)==1:
            self.__sides = sides * self.sides_count
        if self.sides_count == 1:
            self.__radius = self.__sides[0] / math.pi / 2

    def get_color(self, *args):#возвращает список RGB цветов
        return self.__color

    def __is_valid_color(self, list_colors):
        for rgb in list_colors:
            if type(rgb) != int or rgb > 255 or rgb < 0:
                return False
        return True

    def set_color(self, *args):
        list_colors = list(args)
        if Figure.__is_valid_color(self, list_colors) == True:
            self.__color = list_colors

    def __is_valid_sides(self,*args):       # возвращает True если все стороны целые положительные числа
        if len(args) == self.sides_count:   # и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
            for arg in args:
                if type(arg) != int and arg < 0:
                    return False
            return True
        return False

    def get_sides (self): #должен возвращать значения атрибута __sides.
        return list(self.__sides)

    def __len__(self): #должен возвращать периметр фигуры.
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides
    # должен принимать новые стороны, если их количество не равно sides_count, то не изменять, в противном случае - менять.

class Circle(Figure):   #рассчитать исходя из длины окружности (одной единственной стороны).
    sides_count = 1

    def get_square(self):
        return self.get_sides()[0]**2/4/math.pi

class Triangle(Figure):
    sides_count = 3

    def get_square(self): #возвращает площадь треугольника. (можно рассчитать по формуле Герона)
        # p = (a + b + c) / 2
        p = sum(self.get_sides())/2
        # S = (p * (p - a) * (p - b) * (p - c))**(1/2)
        return (p*(p-self.get_sides()[0])*(p-self.get_sides()[1])*(p-self.get_sides()[2]))**(1/2)

class Cube(Figure):
    sides_count = 12

    def get_volume(self): #, возвращает объём куба.
        return self.get_sides()[0]**3

Circle((200, 200, 100), 10)  # (Цвет, стороны)
Circle((200, 200, 100), 10, 14, 18, 25)  # (Цвет, стороны)

# При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count,
# то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.

# Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

"""
Выходные данные (консоль):

[55, 66, 77]
[222, 35, 130]
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[15]
15
216

Примечания (рекомендации):
Рекомендуется сделать дополнительные (свои проверки) работы методов объектов каждого класса.
Делайте каждый класс и метод последовательно и проверяйте работу каждой части отдельно.
Для проверки принадлежности к типу рекомендуется использовать функцию isinstance.
Помните, служебные инкапсулированные методы можно и нужно использовать только внутри текущего класса.
Вам не запрещается вводить дополнительные атрибуты и методы, творите, но не переборщите!
"""