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



# ====================Кореляция в города свыше 1.5 млн ==============================

large_cities = df_cleaned[df_cleaned['population'] > 1.5e6]
print(large_cities)
correlation = large_cities['population'].corr(large_cities['average'])
print(correlation)

"""Корреляция утверждает что связи нет """

# ====================распределние среднего числа преступлений по разным городам ==============================
crime_columns = ['violent_crimes', 'homicides', 'rapes', 'assaults', 'robberies']
df_cleaned['frequency_crimes'] = df_cleaned[crime_columns].sum(axis=1) / len(df_cleaned['report_year'].unique())

plt.figure(figsize=(12, 8))
sns.histplot(data=df_cleaned, x="frequency_crimes", bins=30, kde=True, hue='agency_jurisdiction', multiple='stack')
plt.title('Распределение частот преступлений в различных городах')
plt.xlabel('Частота преступлений')
plt.ylabel('Количество городов')
plt.show()
