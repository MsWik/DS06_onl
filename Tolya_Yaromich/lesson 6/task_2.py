rezults_list = [] 

def enter_results():
    global rezults_list
    while True:
        input_rez = input("Введите результат эксперимента (2 числа через пробел): ")
        if input_rez:
            
            numbers = input_rez.split()
            if len(numbers) == 2:
                rezults_list.append(int(numbers[0]), int(numbers[1]))
                print("Добавьте еще результаты, должно быть четное количество пар")
            else:
                print("Введите два числа через пробел")
        else:
            break 
    if len(rezults_list) % 2 != 0:
        rezults_list = []

def get_sum():
    sum_list = []
    global rezults_list
    for i in range(0, len(rezults_list), 2):
        sum_pair = (rezults_list[i][0] + rezults_list[i + 1][0], rezults_list[i][1] + rezults_list[i + 1][1])
        sum_list.append(sum_pair)
        print (sum_list)
    return sum_list
    
def get_average():
    average_list = []
    global rezults_list
    for i in range(0, len(rezults_list), 2):
        avg_pair = (
            (rezults_list[i][0] + rezults_list[i + 1][0]) / 2,
            (rezults_list[i][1] + rezults_list[i + 1][1]) / 2
        )
        average_list.append(avg_pair)
    return average_list
