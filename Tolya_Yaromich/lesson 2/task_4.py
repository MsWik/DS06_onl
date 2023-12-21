number_input1 = input("Введите четырехзначное число: ")
number_input1=list(str(number_input1))
list_otv=[number_input1[1],number_input1[0],number_input1[3],number_input1[2]]
print("".join(list_otv))