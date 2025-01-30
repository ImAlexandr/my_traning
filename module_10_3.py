# Задача "Банковские операции":

import threading
import random
from time import sleep


# lock = threading.Lock

class Bank:

    def __init__(self, balance: int = 0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            rand_ = random.randint(50, 500)
            self.balance += rand_
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {rand_}. Баланс: {self.balance}.')
            sleep(0.01)

    def take(self):
        for i in range(100):
            rand_ = random.randint(50, 500)
            print(f"Запрос на {rand_}")
            if rand_ <= self.balance:
                self.balance -= rand_
                print(f'Снятие: {rand_}. Баланс: {self.balance}.')
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            sleep(0.01)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
