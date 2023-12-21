

file_name = input("Введите имя файла: ")
numbers = []
try:
    with open(file_name, 'r') as file:   
        content = file.read() 
        words = content.split()  
        for word in words:
            try:
                number = float(word)
                numbers.append(number)
            except ValueError:
                pass  

    print("Список чисел из файла:", numbers)

    print("количество всех чисел:", len(numbers))

    print("количество положительных чисел:", len([x for x in (numbers) if x >0]))

    print("минимальное число:", min(numbers))

    print("максимальное число:", max(numbers))

    print("cумма всех чисел:", sum(numbers))

    print("среднее арифметическое всех чисел с точностью до двух знаков после запятой:", sum(numbers)/ len(numbers))
except FileNotFoundError:
    print("Файл не найден.")
except Exception as e:
    print("Произошла ошибка:", e)
