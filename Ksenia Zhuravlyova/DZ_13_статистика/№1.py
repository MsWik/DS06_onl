
import pandas as pd
import gdown
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


url = 'https://drive.google.com/uc?id=1OPngxMvLVx7krUuLR6YX9TXz0iILah6W'
output = 'report.csv'
gdown.download(url, output, quiet=False)

df = pd.read_csv('report.csv')

df = df.dropna()
per_capita_columns = ['crimes_percapita', 'homicides_percapita', 'rapes_percapita', 'assaults_percapita', 'robberies_percapita']
df[per_capita_columns] = df[per_capita_columns] * 10**(-5)
print(df)
statistica = df.describe()
print(statistica)

df_groups = df.groupby(['report_year', 'agency_code'])
aggregated_data = df_groups.agg({
    'population': 'sum',
    'violent_crimes': 'sum',
    'homicides': 'sum',
    'rapes': 'sum',
    'assaults': 'sum',
    'robberies': 'sum',
    'months_reported': 'mean',
    'crimes_percapita': 'mean',
    'homicides_percapita': 'mean',
    'rapes_percapita': 'mean',
    'assaults_percapita': 'mean',
    'robberies_percapita': 'mean'
}).reset_index()

print(aggregated_data)

aggregated_data['crime_rate'] = aggregated_data['violent_crimes'] / aggregated_data['population']
aggregated_data['homicide_ratio'] = aggregated_data['homicides'] / aggregated_data['violent_crimes']

# График уровня преступности на душу населения по годам
plt.figure(figsize=(10, 6))
for place, group in aggregated_data.groupby('agency_code'):
    plt.plot(group['report_year'], group['crime_rate'], label=place)

plt.title('Crime Rate per Capita Over the Years')
plt.xlabel('Year')
plt.ylabel('Crime Rate per Capita')
plt.legend(loc='upper left')
plt.show()

# График доли убийств среди преступлений по годам
plt.figure(figsize=(10, 6))
for place, group in aggregated_data.groupby('agency_code'):
    plt.plot(group['report_year'], group['homicide_ratio'], label=place)

plt.title('Homicide Ratio Over the Years')
plt.xlabel('Year')
plt.ylabel('Homicide Ratio')
plt.legend(loc='upper left')
plt.show()



df['crime_rate'] = df['crimes_percapita']


crime_types = ['violent_crimes', 'homicides', 'rapes', 'assaults', 'robberies']


for crime_type in crime_types:
    df[crime_type] = df[crime_type] / df['population'] * 100000


for crime_type in crime_types:
    plt.plot(df['report_year'], df[crime_type], label=crime_type)

plt.xlabel('Год')
plt.ylabel('Частота преступлений на душу населения')
plt.title('Изменение частоты различных видов преступлений по годам')
plt.legend()
plt.show()

df['violent_crimes'] = df['violent_crimes'] / df['population'] * 100000
plt.plot(df['report_year'], df['violent_crimes'], label='violent_crimes')

plt.xlabel('Год')
plt.ylabel('Частота преступлений на душу населения')
plt.title('Изменение частоты violent_crimes преступлений по годам')
plt.legend()
plt.show()

df['homicides'] = df['homicides'] / df['population'] * 100000
plt.plot(df['report_year'], df['homicides'], label='homicides')

plt.xlabel('Год')
plt.ylabel('Частота преступлений на душу населения')
plt.title('Изменение частоты homicides преступлений по годам')
plt.legend()
plt.show()


df['rapes'] = df['rapes'] / df['population'] * 100000
plt.plot(df['report_year'], df['rapes'], label='rapes')

plt.xlabel('Год')
plt.ylabel('Частота преступлений на душу населения')
plt.title('Изменение частоты rapes преступлений по годам')
plt.legend()
plt.show()


df['assaults'] = df['assaults'] / df['population'] * 100000
plt.plot(df['report_year'], df['assaults'], label='assaults')

plt.xlabel('Год')
plt.ylabel('Частота преступлений на душу населения')
plt.title('Изменение частоты assaults преступлений по годам')
plt.legend()
plt.show()



df['robberies'] = df['robberies'] / df['population'] * 100000
plt.plot(df['report_year'], df['robberies'], label='robberies')

plt.xlabel('Год')
plt.ylabel('Частота преступлений на душу населения')
plt.title('Изменение частоты robberies преступлений по годам')
plt.legend()
plt.show()

df['city_size'] = pd.cut(df['population'], bins=[0, 500000, float('inf')], labels=['Маленький', 'Крупный'])

# Выберите интересующие вас виды преступлений
crime_types = ['violent_crimes', 'homicides', 'rapes', 'assaults', 'robberies']

# Перезапишите столбцы происшествий на душу населения
for crime_type in crime_types:
    df[crime_type] = df[crime_type] / df['population'] * 100000
    df['violent_crimes'] = df['violent_crimes'] / df['population'] * 100000
    df['homicides'] = df['homicides'] / df['population'] * 100000
    df['rapes'] = df['rapes'] / df['population'] * 100000
    df['assaults'] = df['assaults'] / df['population'] * 100000
    df['robberies'] = df['robberies'] / df['population'] * 100000

# Группировка данных по размеру города
grouped_data = df.groupby('city_size')

# Постройте графики для каждой группы (Маленький и Крупный города)
for name, group in grouped_data:
    for crime_type in crime_types:
        plt.plot(group['report_year'], group[crime_type], label=f'{name}: {crime_type}')

plt.xlabel('Год')
plt.ylabel('Частота преступлений на душу населения')
plt.title('Изменение частоты различных видов преступлений по годам для городов разного размера')
plt.legend()
plt.show()