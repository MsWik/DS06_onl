import pandas as pd


def update(journal: pd.DataFrame) -> pd.DataFrame:
    new_frame = journal[['maths', 'physics', 'computer science']].mean(axis=1)
    new_frame = journal.assign(average=new_frame)
    new_frame = new_frame.sort_values(
        by=['average', 'name'], key=lambda x: x, ascending=[False, True])
    return new_frame


def need_to_work_better(journal: pd.DataFrame) -> pd.DataFrame:
    filtered = journal[journal[['maths', 'physics',
                                'computer science']] == 2].any(axis=1)
    return journal[filtered]


def best(journal: pd.DataFrame) -> pd.DataFrame:
    filtered = journal[['maths', 'physics', 'computer science']].sum(axis=1)
    indexes = filtered[filtered == filtered.aggregate('max')]
    return journal.iloc[indexes.index]


def main():
    columns = ['name', 'maths', 'physics', 'computer science']
    data = {
        'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
        'maths': [5, 4, 5, 2, 4],
        'physics': [4, 4, 4, 5, 5],
        'computer science': [5, 2, 5, 4, 3]
    }
    journal = pd.DataFrame(data, columns=columns)
    filtered = best(journal)
    bad_guys = need_to_work_better(journal)
    updated = update(journal)
    print(journal)
    print(filtered)
    print(bad_guys)
    print(updated)


if __name__ == '__main__':
    main()
