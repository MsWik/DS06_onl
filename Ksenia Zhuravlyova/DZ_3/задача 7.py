
# пустой словарь для представления отношений друзей
friendships = {}

# Считываем дружеские пары и создаем граф отношений
while True:
    line = input().strip()
    if not line:
        break

    person1, person2 = line.split()

    if person1 in friendships:
        friendships[person1].append(person2)
    else:
        friendships[person1] = [person2]

    if person2 in friendships:
        friendships[person2].append(person1)
    else:
        friendships[person2] = [person1]

# Функция для нахождения друзей 2-го уровня
def find_second_level_friends(person):
    second_level_friends = set()
    if person in friendships:
        for friend in friendships[person]:
            if friend in friendships:
                for friend_of_friend in friendships[friend]:
                    if friend_of_friend != person:
                        second_level_friends.add(friend_of_friend)
    return sorted(second_level_friends)

# Выводим список людей и их друзей 2-го уровня
people = sorted(friendships.keys())
for person in people:
    second_level_friends = find_second_level_friends(person)
    if second_level_friends:
        print(f"{person}: " + ", ".join(second_level_friends))









