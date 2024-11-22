# Задача "Всё не так уж просто":

numbers = list(range(1, 16))
primes = list()
not_primes = list()

for i in range(len(numbers)):
    is_primes = True
    if numbers[i] <= 1:
        is_primes = True
    if numbers[i] == 2:
        is_primes = False
    for j in (range(2, numbers[i])):
        is_primes = numbers[i] % j == 0
        break

    if is_primes is True:
        not_primes.append(numbers[i])
    else:
        primes.append(numbers[i])

print('Primes',primes)
print('Not_primes',not_primes)
