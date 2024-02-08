def main():
    with open('secret.txt', 'r') as file:
        message = ""
        for char in file.read():
            char_code = ord(char)
            if char_code < 128:
                message += chr(char_code)
        return message

if __name__ == '__main__':
    print(main())

#Ответ не совпадает с правильным