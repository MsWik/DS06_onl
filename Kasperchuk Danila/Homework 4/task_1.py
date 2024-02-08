def main():
    n = input()
    return "YES" if n == n[::-1] else "NO"

if __name__ == '__main__':
    print(main())