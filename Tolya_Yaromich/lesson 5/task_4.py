import random
nach=1
kon=1000
print("Пишите Больше Меньше или Угадал")
for i in range(10):
    rand=random.randint(nach,kon) 
    print(rand)
    input_resh=input().lower()
    if input_resh=="больше":
        nach=rand
    elif input_resh=="меньше":
        kon=rand
    elif input_resh=="угадал":
        break
    else:
        print("не понял,но продолжу")