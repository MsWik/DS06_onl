reverse_input=input("Ввод:")
value_input = ''.join(char for char in reverse_input if char.isalnum()).lower()
reverse_input = value_input[::-1]
if value_input  == reverse_input:
    print("YES")
else:
    print("NO")