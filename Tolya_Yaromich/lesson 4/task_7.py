
friends = {}
friends_of_friends = {}

while True:
    input_friend = input("ввод имени:")
    if not input_friend:
        break
    name_1, name_2 = input_friend.split()
    
    
    if name_1 not in friends:
        friends[name_1] = []
    friends[name_1].append(name_2)
    
    if name_2 not in friends:
        friends[name_2] = []
    friends[name_2].append(name_1)

for person, friend_list in friends.items():
    friends_of_friends[person] = set()
    for friend in friend_list:
        if friend in friends:
            for friend2 in friends[friend]:
                if friend2 != person and friend2 not in friend_list:
                    friends_of_friends[person].add(friend2)

for person, friend_set in sorted(friends_of_friends.items()):
    friends_list = ', '.join(sorted(friend_set))
    print(f"{person}: {friends_list}")