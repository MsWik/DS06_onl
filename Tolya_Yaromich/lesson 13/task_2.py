import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

df = pd.read_csv('C:/Users/qiarr/Desktop/task/lesson 13/report.csv')
print(df)

# Удалить строки с NaN
df_cleaned = df.dropna()

# Деление значений в колонках "per capita" на 10^5
columns_to_adjust = ['crimes_percapita', 'homicides_percapita', 'rapes_percapita', 'assaults_percapita', 'robberies_percapita']
df_cleaned.loc[:, columns_to_adjust] = df_cleaned.loc[:, columns_to_adjust] / 10**5

print(df_cleaned)

statistics = df_cleaned.describe()
print(statistics)

# Группировка данных по годам
statistics_by_year = df_cleaned.groupby('report_year').describe()

# Вывод статистики по годам
print(statistics_by_year)

columns_of_interest = ['violent_crimes', 'homicides', 'rapes', 'assaults', 'robberies',
                        'crimes_percapita', 'homicides_percapita', 'rapes_percapita', 'assaults_percapita', 'robberies_percapita']
# Преобразование числовых столбцов в числовой тип данных
df_cleaned[columns_of_interest] = df_cleaned[columns_of_interest].apply(pd.to_numeric, errors='coerce')

# Группировка данных по годам
statistics_by_year = df_cleaned.groupby('report_year')[columns_of_interest].mean().reset_index()

# Перезапись столбцов происшествий на душу населения
for column in columns_of_interest:
    per_capita_column = f"{column}"
    df_cleaned[per_capita_column] = df_cleaned[column] / df_cleaned['population'] * 1000  # Умножаем на 1000 для получения per capita на 1000 человек

# Создание графика
plt.figure(figsize=(15, 10))

# Итерация по всем интересующим параметрам и добавление линий на график
for parameter in columns_of_interest:
    per_capita_column = f"{parameter}"
    sns.lineplot(x='report_year', y=per_capita_column, data=df_cleaned, label=per_capita_column,ci=None)

# Добавление легенды и подписей осей
plt.legend(title='Параметры (per capita)')
plt.title('Статистика преступлений на душу населения по годам')
plt.xlabel('Год')
plt.ylabel('Значение')

# Показ графика
plt.show()
"""
Исходя из графиков мы видим что пик преступной деятельности был на примерно 1992 год,
В это время был: Лос-анджелесский бунт,Экономический спад,Высокий уровень безработицы,
Кризис в сфере наркотиков,Политика "Три удара и ты в тюрьме" (Three Strikes and You're Out)

"""