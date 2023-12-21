#Напишите lambda выражение для сортировки списка слов сначала по длине, а затем по алфавиту без учёта регистра.

words = ['веревка', 'дерево', 'яд', 'кот', 'апельсин']
sorted_words = sorted(words, key=lambda x: (len(x), x.lower()))
sorted_words2 = sorted(words, key=lambda x: x.lower())
print(sorted_words, sorted_words2)