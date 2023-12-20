input_list = input("Введите число: ")
rezult_list = []
schet = 1

for index in range(len(input_list) - 1, -1, -1):
    value = input_list[index]
    if value == input_list[index - 1] :
        schet += 1       
    elif index == len(input_list) - 1:
        rezult_list.append([1, input_list[index]])    
    else:
        rezult_list.append([schet, input_list[index]])
        schet = 1

rezult_list = list(reversed(rezult_list))
for i in rezult_list:
    str_i = [str(item) for item in i]
    print(" ".join(str_i))