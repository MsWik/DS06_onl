def is_palindrome():
    n = int(input())
    palindrome = 0

    for _ in range(n):
        s = input()
        if s == s[::-1]:
            palindrome += 1

    print(palindrome)

is_palindrome()

