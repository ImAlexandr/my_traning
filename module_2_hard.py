#   Задание "Слишком древний шифр"

def divider(n):# Вычисление делителей
    div=[]
    for i in range(3,n+1):
        if n % i == 0:
            div.append(i)
    return  div

result=[]
n = int(input('Введите число от 3 до 20: '))
div=divider(n)

for i in range(1,n):
    for element in div:
        if element/2 > i:
            result.append(i)
            result.append(element - i)

res=(''.join([str(item) for item in result]))
print(f"Для числа: {n} шифр: {res}")
# для проверки 20 - 13141911923282183731746416515614713812911