from re import findall
way = 'for_task_5.txt'
l = []
with open(way,'r') as file:
    text = file.read()
    numbers = findall(r'-?\d+',text)
for i in numbers:
    l.append(int(i))
print(f'Содержимое файла {way}:\n',text)
print(len(numbers))
positiv = [number for number in numbers if int(number) > 0]
print(len(positiv))
print(min(l))
print(max(l))
print(sum(l))
print(round(sum(l)/len(l),2))
