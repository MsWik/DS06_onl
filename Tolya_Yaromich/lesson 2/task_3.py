var_input=int(input("Введите число :"))
square_list = []
for i in range(var_input):
    square_list.insert(0,str("* "))
for i in range(var_input):
    print("".join(square_list))