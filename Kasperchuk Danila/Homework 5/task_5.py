def main(filename):
    amount = int()
    more_than_zero = int()
    min_num = int()
    max_num = int()
    sum_of_nums = int()
    arifmetic_mean = int()

    full_list_nums = list()

    with open(filename, "r") as file:
        for line in file:
            for char in line.strip().split(" "):
                full_list_nums.append(char)
        full_list_nums = [int(num) for num in full_list_nums]
        print(len(full_list_nums))
        print(" ".join([str(el) for el in find_positives(full_list_nums)]))
        print(min(full_list_nums))
        print(max(full_list_nums))
        print(round(sum(full_list_nums) / len(full_list_nums), 2))

def find_positives(list_nums):
    new_array = []
    for arr_el in list_nums:
        if arr_el > 0:
            new_array.append(arr_el)
    return new_array  
if __name__ == '__main__':
    main("file.txt")