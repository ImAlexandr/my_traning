# Задача "Функциональное разнообразие":

import random

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))


# [False, True, True, False, False, False, False, False, True, False, False, False, False, False]


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding="UTF-8") as txt_file:
            txt_file.write(str(data_set))
            txt_file.close()

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        x = random.choice(self.words)
        return x


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
