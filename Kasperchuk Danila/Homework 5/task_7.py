def main():
    amount = int(input())
    list_nums = list()
    for i in range(amount):
        list_nums.append(int(input()))
    count = 0

    for num in list_nums:
        if is_simple(num):
            count += 1
        else:
            pass

    return count


def is_simple(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
        
if __name__ == '__main__':
    print(main())