# Задача "Потоковая запись в файлы"
from time import sleep
import time
import threading


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding="UTF-8") as txt_file:
        for i in range(1, word_count + 1):
            txt_file.write('Какое-то слово № ' + str(i) + '\n')
            sleep(0.1)
        txt_file.close()
        print("Завершилась запись в файл:", file_name)


start_time = time.time()

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

finish_time = time.time()
print(f'Работа потоков {finish_time - start_time}')
print()

start_time = time.time()

thread5 = threading.Thread(target=wite_words, args=(10, 'example5.txt'), daemon=True)  # дополнительный поток
thread6 = threading.Thread(target=wite_words, args=(30, 'example6.txt'), daemon=True)  # дополнительный поток
thread7 = threading.Thread(target=wite_words, args=(200, 'example7.txt'), daemon=True)  # дополнительный поток
thread8 = threading.Thread(target=wite_words, args=(100, 'example8.txt'), daemon=True)  # дополнительный поток
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread5.join()
thread6.join()
thread7.join()
thread8.join()

finish_time = time.time()

print(f'Работа потоков {finish_time - start_time}')
