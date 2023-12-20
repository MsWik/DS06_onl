global_list=[]
r=True
while r==True:
    input_1=(input("введите придорожных зверюшек или ничего для конца ввода: ")).split()
    if not input_1:
        r=False
    else:
        global_list.append(input_1)
        
filtered_list = [s for s in global_list if "зайка" in s]
if filtered_list:
    character_list=[]
    for i in filtered_list:
        character_list.append(list("".join(i)))     
    shortest_string = min(character_list, key=len)
    index =  character_list.index(shortest_string)
    shortest_string_len=len(shortest_string)
    print("Самая короткая строка, содержащая 'зайка':", " ".join(filtered_list[index]),shortest_string_len)
else:
    print("Нет строк, содержащих 'зайка' в списке.")            
    

