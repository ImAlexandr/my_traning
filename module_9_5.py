# Задача "Range - это просто"

class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self  # и возвращающий сам объект итератора.

    def __next__(self):
        if self.step > 0:
            if self.stop < self.start or self.stop < self.pointer:
                raise StopIteration
            if self.pointer < self.stop:
                self.pointer += self.step
                return self.pointer - self.step

        if self.step < 0:
            if self.stop > self.start or self.stop > self.pointer:
                raise StopIteration
            if self.pointer > self.stop:
                self.pointer += self.step
                return self.pointer - self.step

        if self.pointer == self.start or self.pointer == self.stop:
            self.pointer += self.step
            return self.pointer - self.step


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()

"""
Вывод на консоль:
Шаг указан неверно
-5 -4 -3 -2 -1 0 1
6 8 10 12 14
5 4 3 2 1
"""
