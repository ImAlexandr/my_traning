# Задача "За честь и отвагу!"

import threading
import time


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        super().__init__(name=name)
        self.power = power
        self.enemy = 100
        self.days = 0

    def days(self):
        self.enemy -= self.power
        self.days += 1
        time.sleep(1)

    def run(self):
        print(f' {self.name}, на нас напали!"')
        Knight.days(self)
        while self.enemy:
            print(f' {self.name} сражается {self.days} ..., осталось {self.enemy} воинов.')
            Knight.days(self)
        print(f' {self.name}, одержал победу спустя {self.days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
time.sleep(.01)
second_knight.start()
first_knight.join()
second_knight.join()
time.sleep(0.5)
print(f'Все битвы закончились!')
