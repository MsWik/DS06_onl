def simple(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False

    return True
input_main = int(input())  
count = 0 
for _ in range(input_main):
    number = int(input()) 
    if simple(number):
        count += 1  
print("ответ:",count) 