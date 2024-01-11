friends = []
d = {}
while True:
    line = input()
    if line == "":
        break
    friends.append(line)


print(friends)
for i in friends:
    for name in i.split():
        if name in d:
            d[name] = name
            continue
        d[name] = ''
print(d)
