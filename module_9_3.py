first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = [(abs(len(x)) - len(y)) for x, y in zip(first, second) if len(x) - len(y) != 0]

second_result = [len(first[i]) == len(second[i]) for i in range(len(first))]

print(list(first_result))
print(list(second_result))

"""
Вывод в консоль:
[1, 2]
[False, False, True]
"""
