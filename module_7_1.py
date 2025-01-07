# Задача "Учёт товаров":

from pprint import pprint
import os.path


class Product:

    def __init__(self, *args):
        self.name = str(args[0])
        self.weight = float(args[1])
        self.category = str(args[2])

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    z = str

    def get_products(self):
        __file_name = 'products.txt'
        if os.path.exists(__file_name):     # Проверка на существование файла
            file = open(__file_name, 'r')
            z = file.read()  # возвращает единую строку со всеми товарами из файла __file_name.
            file.close()
            return z
        else:
            file = open(__file_name, "a")
            file.close()

    def add(self, *products):
        for i in products:  # Перебираем продукты
            i1 = str(i).split(',')[0]  # Отделили название
            z = str(s1.get_products()).replace("\n", " ")  # Убрали перенос строки
            if i1 in z:
                print(f'Продукт: {i1} уже есть в магазине')
            else:
                __file_name = 'products.txt'
                file = open(__file_name, 'a')
                file.write(str(i) + '\n')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)  # __str__

s1.add(p1, p2, p3)
print(s1.get_products())

# ***********************************************************************
# Вывод на консоль:
#
# Первый запуск:
#
# Spaghetti, 3.4, Groceries
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables
#
# Второй запуск:
#
# Spaghetti, 3.4, Groceries
# Продукт Potato уже есть в магазине
# Продукт Spaghetti уже есть в магазине
# Продукт Potato уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables
# Как выглядит файл после запусков (см. файл домашнего задания)
#
