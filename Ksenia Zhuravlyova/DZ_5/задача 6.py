numbers = input().split()
even_numbers = filter(lambda x: sum(map(int, x)) % 2 == 0, numbers)

for number in even_numbers:
    print(number)


