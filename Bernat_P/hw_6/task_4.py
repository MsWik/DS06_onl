string = 'мама мыл мбма'
print(sorted(string.split(), key=len))

value = '123 432 143 17'
if __name__ == '__main__':
    print(sorted([int(i) for i in value.split() if sum([int(j) for j in i]) % 2 == 0]))

# filter_even_sum = lambda num: sum(int(digit) for digit in str(num)) % 2 == 0


