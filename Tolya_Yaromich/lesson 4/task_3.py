count=int(input("Введите число :"))
Zyac_lengs=0
for _ in range (count):
    input_animal=input("Введите зверей :")
    Zyac_lengs+=(len(list(filter(lambda x:x=="зайка" , input_animal.split()))))
print(Zyac_lengs)