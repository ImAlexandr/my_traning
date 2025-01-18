# Задача "Ошибка эволюции":

import random


class Animal:  # - класс описывающий животных.
    live = True
    sound = None  # - звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0  # - степень опасности существа
    _cords = [0, 0, 0]  # - координаты в пространстве.

    def __init__(self, speed):
        self.speed = speed

    def move(self, dx, dy, dz):
        self._cords[0] = dx * self.speed
        self._cords[1] = dy * self.speed
        if dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
            return
        self._cords[2] = dz * self.speed

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {int(self._cords[2])}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        if self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):  # - класс описывающий птиц.
    beak = True  # - наличие клюва

    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 4)} eggs for you")


class AquaticAnimal(Animal):  # - класс описывающий плавающего животного
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self.speed /= 2
        self._cords[2] -= abs(dz) * self.speed


class PoisonousAnimal(Animal):  # - класс описывающий ядовитых животных. Наследуется от Animal.
    _DEGREE_OF_DANGER = 8.


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = "Click-click-click"  # - звук, который издаёт утконос


db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
"""
Вывод на консоль:
True
True
Click-click-click
Be careful, i'm attacking you 0_0
X: 10 Y: 20 Z: 30
X: 10 Y: 20 Z: 0
Here are(is) 3 eggs for you # Число может быть другим (1-4)

По итогу мы должны получить живого утконоса с клювом, атакующего и издающего странные звуки.
После чего утконос совершает манёвры и ныряет.
Теперь утконос в безопасности, он откладывает яйца для будущего потомства.

Примечания:
Будьте внимательней, когда вызываете методы классов родителей в классе наследнике при множественном наследовании:
при обращении через super() методы будут искаться сначала в первом, потом во втором и т.д. классах по mro().
При определении порядка наследования обратите внимание на то, что утконос атакует "Be careful, i'm attacking you 0_0"

"""
