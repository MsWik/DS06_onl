def main():
    n = int(input())
    list_lines = list()

    for i in range(n):
        list_lines.append(int(input()))
    
    count = 0
    for num in list_lines:
        if str(num) == str(num)[::-1]:
            count += 1
    return count

if __name__ == '__main__':
    print(main())