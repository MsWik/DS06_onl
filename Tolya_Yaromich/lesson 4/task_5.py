
def init():
    result = None

    def calculate(expression):
        try:
            return eval(expression)
        except ZeroDivisionError:
            return "Деление на ноль"
            
        except Exception:
            return "Ошибка вычисления"
            

    input_list = input("Введите числа и знаки через пробел: ").split()

    while any(isinstance(char, str) for char in input_list):
        for index, value in enumerate(input_list):
            if isinstance(value, str) and value in ['+', '-', '*', '/']:
                
                expression = f"{input_list[index-2]} {value} {input_list[index-1]}"
                result = calculate(expression)
                input_list[index-2] = str(result)
                input_list.pop(index-1)
                input_list.pop(index-1)  
            if len(input_list) ==1 :
                print("Результат:", result)
                input_list = [int(item) for item in input_list]
                break          
    else:
            init()                
    
init()