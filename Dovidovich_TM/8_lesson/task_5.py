import pandas as pd


def clear_string(string: str) -> str:
    string = string.lower()
    trash = ',.!?'
    for char in trash:
        string = string.replace(char, '')
    return string


def length_stats(string: str):
    list_words = list(set(clear_string(string).split()))
    list_words.sort(key=lambda x: x)
    words = pd.Series([len(x) for x in list_words])
    words.rename(index={i: list_words[i]
                 for i in range(len(list_words))}, inplace=True)
    odd = words[words.apply(lambda x: x % 2 != 0)]
    even = words[words.apply(lambda x: x % 2 == 0)]
    return odd, even


def main():
    odd, even = length_stats(
        'Лес, опушка, странный домик. Лес, опушка и зверушка.')
    print(odd)
    print(even)


if __name__ == '__main__':
    main()
