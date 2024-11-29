# Задача "Распаковка":

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    return ()

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [(1,2,3), {4:5, 6:7, 8:9}, [10,11,12]]
print_params(*values_list)

values_dict = {'a' : 'Word', 'b' : True, 'c' : 15.715}
print_params(**values_dict)

values_list_2 = [154.32, 'Строчка' ]
print_params(*values_list_2, 42)