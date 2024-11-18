# Задача "Все ли равны?":
first, second, third=map(int, input('Введите через запятую три числа:').split(","))
if first==second==third:
    n=3
elif first==second or first==third or second==third:
    n=2
else:
    n=0
print(f'Между собой равны {n} числа')