def main():
    string = input().replace(" ",'')
    print("YES") if string == string[::-1] else print("NO")

if __name__ == "__main__":
    main()
