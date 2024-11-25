# Задача "Всё не так уж просто":

numbers = list(range(1, 16))
primes = list()
not_primes = list()

for i in range(len(numbers)):
    a=numbers[i]
    is_primes = True
    if numbers[i] <= 1:
        continue
    if numbers[i] == 2:
        pass

    for j in (range(2, numbers[i])):
        if numbers[i] % j == 0:
            is_primes = False
            break

    if is_primes is True:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

print('Numbers',numbers)
print('Primes',primes)
print('Not_primes',not_primes)
