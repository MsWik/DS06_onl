import pandas as pd
import string #--Я узнал про встроенную библиотеку string в которой можно удобно выделить только знаки пунктуации за один метод

def length_stats(text):
    
    sorted_words = sorted((''.join(char for char in text.lower() if char not in string.punctuation and not char.isdigit())).split())
    
    word_lengths = pd.Series([len(word) for word in sorted_words], index=sorted_words, name='Длина слова')
    
    return word_lengths

print(length_stats(input("Ведите текст: ")))
