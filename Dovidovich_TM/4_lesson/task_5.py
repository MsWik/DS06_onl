def main():
    stack = list()
    postfix = input().split()
    for element in postfix:
        if element not in '+-*/':
            stack.append(int(element))
        else:
            match (element):
                case '+': stack.append(stack.pop()+stack.pop())
                case '-': stack.append(stack.pop()-stack.pop())
                case '*': stack.append(stack.pop()*stack.pop())
                case '/': stack.append(stack.pop()/stack.pop())
    print(int(stack.pop()))


if __name__ == "__main__":
    main()
