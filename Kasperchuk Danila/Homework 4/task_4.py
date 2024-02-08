def main():
    n = list(input())
    keys = []
    values = []
    current_num = int()
    current_count = int()
    for i in n:
        
        if i == current_num:
            current_count += 1
        else:
            keys.append(current_num)
            values.append(current_count)
            current_num = i
            current_count = 1

    return [keys, values]

    
if __name__ == '__main__':
    print(main())