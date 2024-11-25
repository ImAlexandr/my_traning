# Задача "Счётчик вызовов"

def count_calls ():# Подсчитывает вызовы остальных функций
    global calls
    calls += 1
    return calls

def string_info (word):
    count_calls()
    tuple_=(len(word), word.lower(), word.upper())
    return (tuple_)

def is_contains (word, list_):
    count_calls()
    lowercase_list = [s.lower() for s in list_]
    flag = False
    if lowercase_list.count(word.lower()):
        flag=True
    return (flag)

calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Incomprehensibility'))
print()
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(is_contains('QueeN', ['pawn', 'king', 'queen', 'rook', 'knight']))
print()
print(calls)