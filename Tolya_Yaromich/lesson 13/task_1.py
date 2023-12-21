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



columns_of_interest = ['violent_crimes', 'homicides', 'rapes', 'assaults', 'robberies',
                        'crimes_percapita', 'homicides_percapita', 'rapes_percapita', 'assaults_percapita', 'robberies_percapita']
#---из-за большого количества параметров,как я понял на одном графике есть ограниение по линиям,он отказывается показывать их больше 6
# Создание графика для одного параметра
plt.figure(figsize=(10, 6))
df_to_plot = pd.DataFrame()
for parameter in columns_of_interest:
    df_to_plot[parameter] = df_cleaned[parameter]

# Использование sns.lineplot для построения графиков для всех параметров
for parameter in columns_of_interest:
    sns.lineplot(x='report_year', y=parameter, data=df_cleaned, label=parameter,ci=None)


# Добавление легенды и подписей осей
plt.legend(title='Параметры')
plt.title('Статистика преступлений по годам')
plt.xlabel('Год')
plt.ylabel('Значение')

# Показ графика
plt.show()


"""
Исходя из графиков мы видим что пик преступной деятельности был на примерно 1992 год,где ообенно выделялись
Нападения ,насильственные убийства ,а также грабеж
также можно сделать вывод что количество нападений по итогу увелиличлось со времен 1975г
"""