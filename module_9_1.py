# Задача "Вызов разом":

def apply_all_func(int_list, *functions):
    results = {}
    for f in functions:
        key = f.__name__
        value = f(int_list)
        results[key] = value
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
