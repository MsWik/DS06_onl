N = int(input())  # дети, любящие манку
M = int(input())  # дети, любящие овсянку
manka = ['Васечкин', 'Иванов', 'Петров']
ovs = ['Васечкин', 'Иванов', 'Петров']
children = ['Васечкин', 'Иванов', 'Петров', 'Михалов', 'Васильев']

# Создаем два пустых множества для фамилий детей, любящих каждый вид каши
manna_lovers = set(manka)
ovsyanka_lovers = set(ovs)

# Считываем фамилии детей и добавляем их в соответствующие множества
for i in range(N):
    name = children[i]
    if name in manna_lovers:
        manna_lovers.add(name)

for i in range(M):
    name = children[i]
    if name in ovsyanka_lovers:
        ovsyanka_lovers.add(name)

# Находим детей, которые любят только один вид каши
only_manna_lovers = set(children) - ovsyanka_lovers
only_ovsyanka_lovers = set(children) - manna_lovers

# Выводим количество таких детей
if only_manna_lovers or only_ovsyanka_lovers:
    print(len(only_manna_lovers) + len(only_ovsyanka_lovers))
else:
    print("Таких нет")


