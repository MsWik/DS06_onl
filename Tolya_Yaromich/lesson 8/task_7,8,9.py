import pandas as pd
columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'physics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data, columns=columns)
def best(journal):
    filtered_journal = journal.loc[(journal['maths'] >= 4) & (journal['physics'] >= 4) & (journal['computer science'] >= 4)]
    return filtered_journal
def  need_to_work_better(journal):
    filtered_journal = journal.loc[(journal['maths'] <= 2) | (journal['physics'] <= 2) | (journal['computer science'] <= 2)]
    return filtered_journal
def  update(journal):
    journal['average'] = (journal['maths'] + journal['physics']+ journal['computer science'])/3
    REjournal = journal.sort_values(by=['average', 'name'],ascending=[False, True])
    return  REjournal

filtered = best(journal)
filtered2 = need_to_work_better(journal)
filtered3 =update(journal)
print("<----------------------------------------------")
print(journal)
print("--------------------|best|---------------------")
print(filtered)
print("--------------------|losers|-------------------")
print(filtered2)
print("--------------------|average|-------------------")
print(filtered3)