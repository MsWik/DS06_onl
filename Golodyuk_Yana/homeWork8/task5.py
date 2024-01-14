# 5
# продумайте функцию length_stats, которая получает текст,
# а возвращает пару объектов Series со словами в качестве индексов
# и их длинами в качестве значений.
# Все слова в тексте предварительно переведите в нижний регистр,
# избавьтесь от знаков препинания и цифр,
# а также отсортируйте в лексикографическом порядке.

import string
import pandas as pd
from typing import Tuple


def lenght_stats(s: str) -> Tuple[pd.Series, pd.Series]:
    words = (
        "".join(
            [
                char
                for char in s
                if not char in string.punctuation and not char.isdigit()
            ]
        )
        .lower()
        .split()
    )
    odd = sorted({word for word in words if len(word) % 2})
    even = sorted({word for word in words if len(word) % 2 == 0})
    odd = pd.Series(data=[len(word) for word in odd], index=odd)
    even = pd.Series(data=[len(word) for word in even], index=even)
    return odd, even


odd, even = lenght_stats("Лес, опушка, странный домик. Лес, опушка и зверушка.")
print(odd)
print(even)