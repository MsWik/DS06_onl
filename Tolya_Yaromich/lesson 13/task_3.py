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
columns_of_interest = ['violent_crimes', 'homicides', 'rapes', 'assaults', 'robberies',
                        'crimes_percapita', 'homicides_percapita', 'rapes_percapita', 'assaults_percapita', 'robberies_percapita']
df_subset = df[columns_of_interest]
df['average'] = df_subset.mean(axis=1)
df_average = df[['report_year', 'average']].copy()
# ====================ГРАФИК==============================

plt.figure(figsize=(10, 6))
sns.lineplot(x='report_year', y="average", data=df_average, label='crimes_percapita')
plt.legend(title='Параметры')
plt.title('Статистика преступлений по годам')
plt.xlabel('Год')
plt.ylabel('Значение')
plt.show()


