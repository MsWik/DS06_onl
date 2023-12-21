# Я надеюсь я правильно понял задание и речь идет о раздядах десятков и разядах чисел где на вывод требуется именно разаяд чисел
# так как в задаче сказано что "он хочет научить сложению остальных ребят и просит написать программу, которая поможет ему в качестве наглядного материала."
# решение было устроено по методу переноса разряда начиная с конца вводимого числа
number_input1 = input("Введите первое число: ")
number_input2 = input("Введите второе число: ")
number_input1=list(str(number_input1))
number_input2=list(str(number_input2))
list_otv=[]
for i,j in zip(reversed(number_input1),reversed(number_input2)):
    tmp = int(i) + int(j)
    if tmp>9:
        tmp=tmp-10    
    list_otv.insert(0,str(tmp))    
print("".join(list_otv))