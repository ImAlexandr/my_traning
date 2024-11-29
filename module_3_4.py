# Задача "Однокоренные":

def single_root_words(root_word,*other_words):
    same_words = []

    for word in other_words:
        count_1 = (root_word.lower().count(word.lower()))
        count_2 = (word.lower().count(root_word.lower()))
        if count_1 > 0 or count_2 > 0:
            same_words.append(word)
    return (same_words)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)