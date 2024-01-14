# Польский калькулятор

from typing import List

def foo(list: List) -> int:
    stack = []
    for element in list:
        if element.isdigit():
            stack.append(int(element))
        else: 
            match (element):
                case '+': 
                    stack.append(stack.pop() + stack.pop())  
                case '-': 
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)  
                case '*': 
                    stack.append(stack.pop() * stack.pop())  
                case '/': 
                    a = stack.pop
                    b = stack.pop
                    stack.append(b / a)            

    return int(stack.pop())

if __name__ == ("__main__"):
    print(foo(['7', '3', '2', '*', '-']))