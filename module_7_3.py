# Задача "Найдёт везде":

import os.path
import io
from time import sleep


class WordsFinder(object):

    def __init__(self, *args):
        file_names = []
        for arg in args:
            file_names.append(arg)
        self.files = file_names
        self.all_words = {}

    def get_all_words(self):
        all_words = {}
        for name in self.files:
            words = []
            with open(name, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(str.maketrans("", "", ",.=!?;:"))
                    line = line.replace(' - ', '')
                    words += line.split()
                all_words[name] = words
        self.all_words = all_words
        return all_words

    def find(self, word):
        find_words = {}
        dict_ = self.all_words
        for key, value in dict_.items():
            if word.lower() in value:
                find_words[key] = value.index(word.lower()) + 1
                continue
        return find_words

    def count(self, word):
        count_words = {}
        dict_ = self.all_words
        for key, value in dict_.items():
            if word.lower() in value:
                count_words[key] = value.count(word.lower())
                continue
        return count_words


print('Разместите рядом с module_7_3.py и текстовые файлы: test_file.txt, file1.txt, file2.txt, file3.txt')
sleep(3)

# finder2 = WordsFinder('test_file.txt')
finder2 = WordsFinder('test_file.txt', 'file1.txt', 'file2.txt', 'file3.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
