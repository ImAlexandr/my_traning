# Задача "Записать и запомнить":

from pprint import pprint
import os.path
import io

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    line_number = 1
    number_byte = 0
    item = {}
    key = ()
    for element in strings:
        key = (line_number, number_byte)
        item[key] = element
        file.write(element + '\n')
        line_number += 1
        number_byte = file.tell()
    file.close()
    return item

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

for elem in result.items():
     print(elem)

# Вывод на консоль:
#
# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')