# 9

# Напишите функцию update, которая добавляет к данным столбец average,
# содержащий среднюю оценку ученика, а также сортирует данные по убыванию этого столбца,
# а при равенстве средних — по имени лексикографически.

import pandas as pd


def update(data: pd.DataFrame):
    data["average"] = data.apply(
        lambda x: (x["maths"] + x["physics"] + x["computer science"]) / 3, axis=1
    )

    return data.sort_values(by=["average", "name"], ascending=[False, True])


columns = ["name", "maths", "physics", "computer science"]
data = {
    "name": ["Иванов", "Петров", "Сидоров", "Васечкин", "Николаев"],
    "maths": [5, 4, 5, 2, 4],
    "physics": [4, 4, 4, 5, 5],
    "computer science": [5, 2, 5, 4, 3],
}
journal = pd.DataFrame(data, columns=columns)
filtered = update(journal)
print(journal)
print(filtered)
