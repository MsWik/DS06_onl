# 7
# Данные об успеваемости представлены DataFrame со столбцами:
# name — имя;
# maths — оценка по математике;
# physics — оценка по физике;
# computer science — оценка по информатике.
# Напишите функцию best, которая фильтрует всех «ударников» в журнале.
# Напишите функцию need_to_work_better, которая выбирает тех, у кого есть хотя бы одна двойка.
# Напишите функцию update, которая добавляет к данным столбец average,
# содержащий среднюю оценку ученика, а также сортирует данные по убыванию этого столбца,
# а при равенстве средних — по имени лексикографически.

import pandas as pd


def best(data: pd.DataFrame) -> pd.DataFrame:
    data["total_score"] = data.apply(
        lambda x: x["maths"] + x["physics"] + x["computer science"], axis=1
    )
    filter_value = data["total_score"].max()

    return data[data["total_score"] == filter_value].drop("total_score", axis=1)


columns = ["name", "maths", "physics", "computer science"]
data = {
    "name": ["Иванов", "Петров", "Сидоров", "Васечкин", "Николаев"],
    "maths": [5, 4, 5, 2, 4],
    "physics": [4, 4, 4, 5, 5],
    "computer science": [5, 2, 5, 4, 3],
}
journal = pd.DataFrame(data, columns=columns)
filtered = best(journal)
print(journal)
print(filtered)
