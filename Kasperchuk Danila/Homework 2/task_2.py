def main():
    list_nums = input().split()
    list_nums[0], list_nums[1] = list_nums[1], list_nums[0]
    prepared_string = " ".join(list_nums)
    return prepared_string
    

if __name__ == '__main__':
    print(main())