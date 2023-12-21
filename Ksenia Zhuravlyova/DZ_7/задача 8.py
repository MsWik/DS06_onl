# Вывод
#        name  maths  physics  computer science
# 0    Иванов      5        4                 5
# 1    Петров      4        4                 2
# 2   Сидоров      5        4                 5
# 3  Васечкин      2        5                 4
# 4  Николаев      4        5                 3
#        name  maths  physics  computer science
# 1    Петров      4        4                 2
# 3  Васечкин      2        5                 4

import pandas as pd

def need_to_work_better(df):
    filtered = df[(df['maths'] <= 2)| (df['physics'] <= 2) | (df['computer science'] <= 2)]
    return filtered

columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'physics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data, columns=columns)
filtered = need_to_work_better(journal)
print(journal)
print(filtered)