# В этот раз продумайте функцию length_stats, которая получает текст,
# а возвращает пару объектов Series со словами в качестве индексов и их длинами в качестве значений.
# Все слова в тексте предварительно переведите в нижний регистр, избавьтесь от знаков препинания и цифр,
# а также отсортируйте в лексикографическом порядке.
# odd, even = length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.')
# print(odd)
# print(even)
# Вывод
# домик    5
# и        1
# лес      3
# dtype: int64
# зверушка    8
# опушка      6
# странный    8
# dtype: int64

import pandas as pd
import string

def length_stats(text):
    text = text.lower()

    text = ''.join(char for char in text if char not in string.punctuation and not char.isdigit())


    words = text.split()


    words.sort()

    # Создаем объект Series с индексами-словами и значениями-длинами слов
    series = pd.Series([len(word) for word in words], index=words)

    # Разделяем слова на четные и нечетные по длине
    odd = series[series.index.str.len() % 2 != 0]
    even = series[series.index.str.len() % 2 == 0]

    return odd, even

text = 'Лес, опушка, странный домик. Лес, опушка и зверушка.'
odd, even = length_stats(text)
print(odd)
print(even)

