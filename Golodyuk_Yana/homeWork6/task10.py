# Задача 10

# Напишите функцию make_linear,
# которая принимает список списков и возвращает его "выпрямленное" представление.


def make_linear(l):
    if not isinstance(l, list):
        return [l]

    answer = []
    for elm in l:
        answer += make_linear(elm)
    return answer


if __name__ == "__main__":
    l = [1, [1, 2, 3], [2, [3, [[5]]]], 6]
    print(make_linear(l))