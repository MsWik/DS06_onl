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






# ====================СРеднее==============================
columns_of_interest = ['crimes_percapita', 'homicides_percapita', 'rapes_percapita', 'assaults_percapita', 'robberies_percapita']
df_subset = df_cleaned[columns_of_interest]
df_cleaned['average'] = df_subset.mean(axis=1)
df_average = df_cleaned[['population', 'average']].copy()
 
print(df_average)

# ====================Сводная таблица==============================
df_cleaned['city_category'] = pd.cut(df_cleaned['population'], bins=[ 100000, 500000, 1000000, float('inf')],
                                     labels=[ 'Средний', 'Крупный', 'Очень крупный'])
columns_of_interest = ['crimes_percapita', 'homicides_percapita', 'rapes_percapita', 'assaults_percapita', 'robberies_percapita']
df_cleaned['average'] = df_subset.mean(axis=1)
pivot_table = pd.pivot_table(df_cleaned, values='average', index='city_category', aggfunc='mean')
print(pivot_table)
# ====================ГРАФИК==============================

plt.figure(figsize=(10, 6))
sns.lineplot(x='population', y="average", data=df_average, label='crimes_percapita')
plt.legend(title='Параметры')
plt.title('Статистика преступлений по популяции ')
plt.xlabel('Популяция млн')
plt.ylabel('Значение')
plt.show()

# ====================График для сводной таблицы=======
plt.figure(figsize=(12, 8))
sns.barplot(x='city_category', y="average", data=pivot_table, label='crimes_percapita')
plt.title('Статистика преступлений по категориям городов')
plt.xlabel('Виды преступлений')
plt.ylabel('Среднее значение')
plt.legend(title='Категория города')
plt.show()

# ====================График regplot=======
plt.figure(figsize=(10, 6))
sns.regplot(x='population', y='average', data=df_average, scatter_kws={'s': 50}) 
plt.title('Зависимость среднего значения преступлений от популяции')
plt.xlabel('Популяция (млн)')
plt.ylabel('Среднее значение преступлений')
plt.show()

crime_columns = ['violent_crimes', 'homicides', 'rapes', 'assaults', 'robberies']

df_cleaned['frequency_crimes'] = df_cleaned[crime_columns].sum(axis=1) / len(df_cleaned['report_year'].unique())
# Рассчет корреляции Пирсона
correlation_1 = df_cleaned['population'].corr(df_cleaned['frequency_crimes'])
correlation_2 = df_average['population'].corr(df_average['average'])
print(f"Корреляция между популяцией и средним значением преступности: {correlation_1}")
print(f"Корреляция между популяцией и средним значением преступности: {correlation_2}")
"""Корреляция утверждает что связь у популяции города и частотой преступлений есть связь  """