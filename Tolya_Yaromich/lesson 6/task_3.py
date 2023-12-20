numbers = [123, 4555252356, 7866649, 14, 34, 56]

filtered_numbers = filter(lambda x: sum(int(i) for i in str(x)) % 2 == 0, numbers)

# Преобразовываем итератор в список
filtered_numbers_list = list(filtered_numbers)

print(filtered_numbers_list)
