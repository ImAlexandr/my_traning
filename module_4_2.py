# Домашнее задание по уроку "Пространство имен"

def test_function (args):

    def inner_function(args):
        print("Я в области видимости функции test_function")
        return

    inner_function(2)
    return
test_function(4)
# inner_function(2)  # функция inner_function вне функции test_function не вызывается