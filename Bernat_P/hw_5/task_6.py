str_with_zaila = []
for _ in range(3):
    s = input().split()
    for word in s:
        if word == 'зайка':
            if len(str_with_zaila) < len(s):
                str_with_zaila = s

print(*str_with_zaila,len(''.join(str_with_zaila)) )

            