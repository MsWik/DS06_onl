N = int(input("Введите N: "))
M = int(input("Введите M: "))

first_list = []
second_list = []
print("Введите фамилии для N:")

for i in range(N):
    last_name = input(f"Фамилия {i + 1}: ")
    first_list.append(last_name)
    
print("Введите фамилии для M:")
for i in range(M):
    last_name = input(f"Фамилия {i + 1}: ")
    second_list.append(last_name)
combined_list = first_list + second_list
unique_names = []

for i in combined_list:
    count = combined_list.count(i)
    if count == 1:
        unique_names.append(i)
if len(unique_names)==0:
    print("Таких нет")
else:
    print(len(unique_names))


