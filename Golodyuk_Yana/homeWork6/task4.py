# Задача 4

# Напишите lambda выражение для сортировки списка слов сначала по длине,
# а затем по алфавиту без учёта регистра.

def sorted_list(s: str):
    print(sorted(s.split(), key=lambda x: (len(x), x.lower())))

if __name__ == "__main__":
    text = 'мама мыла раму яяяяяяяяяяя якушев яяяАяяяяяяя'
    sorted_list(text)