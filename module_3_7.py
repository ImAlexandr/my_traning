# Задание "Раз, два, три, четыре, пять .... Это не всё?

def calculate_structure_sum(args):

    global summa

    if isinstance(args, int | float | bool):
        summa += args

    elif isinstance(args, str):
        summa += len(args)

    elif isinstance(args, list):
        for element in args:
            calculate_structure_sum(element)

    elif isinstance(args, tuple | set):
        element = list (args)
        calculate_structure_sum(element)

    elif isinstance(args, dict):
        for key in args.keys():
            calculate_structure_sum(key)

        for value in args.values():
            calculate_structure_sum(value)

    return summa


summa = 0
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(f'{result=}')

# Выходные данные (консоль): 99
