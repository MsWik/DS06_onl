import pandas as pd
import chardet
from scipy import stats
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
"""
1. Анализ данных, необходимые корректировки. 
2. Обработать пропуски. 
3. Оценить выбросы. 
4. Корреляция. 
5. Тест на нормальность распределения.
6. Масштабировать и стандартизировать данные.
7. Разделите данные на тренрровачную и тестовую выборку.
8. При обработке пропусков/выбросов/скалировании тестовую и тренировачную выборку обрабатывать отдельно.
        необходимо подготовить датасет к обучению
"""
file_path = 'C:/Users/qiarr/Desktop/task/lesson 16/credit_train.csv'

# Чтение файла с учетом кодировки cp1251 что я определил со посощью библотеки chardet
df = pd.read_csv(file_path, encoding='cp1251', delimiter=';')

df_cleaned = df.dropna() #-очищаем датасет от пропусков

pd.set_option("display.max_columns", 50) # настройка отображения датасета

columns_to_check = ['score_shk', 'credit_sum', 'monthly_income']# Список колонок, которые нужно очистить от выбросов



# Заменяем запятые на точки и приводим к типу float для того чтобы работат ьс числовыми данными в датасете
for column in columns_to_check:
    df_cleaned[column] = df_cleaned[column].apply(lambda x: float(str(x).replace(',', '.')))


# Очистка данных от выбросов
for column in columns_to_check:
    lower_bound = df_cleaned[column].mean() - 2.5 * df_cleaned[column].std()
    upper_bound = df_cleaned[column].mean() + 2.5 * df_cleaned[column].std()
    
    # Фильтрация данных по границам
    df_cleaned = df_cleaned[(df_cleaned[column] >= lower_bound) & (df_cleaned[column] <= upper_bound)]

numerical_columns = df_cleaned.select_dtypes(include='number')

# Вычисление корреляции
correlation_matrix = numerical_columns.corr()
# Вывод результата корреляии
print(correlation_matrix)
"""
Исходя из матрицы корреляций,самое большое значение  0.326713 у  monthly_income и credit_sum
"""


#--------------------------------------------------------------------------------------------------
# Тест Шапиро-Уилка для проверки нормальности распределения
stat, p_value = stats.shapiro(numerical_columns)

alpha = 0.05
if p_value > alpha:
    print('Принимаем нулевую гипотезу: данные имеют нормальное распределение')
else:
    print('Отклоняем нулевую гипотезу: данные не имеют нормальное распределение')
    
    
#-----------------Масштабировать и стандартизировать данные.------------------------------------------
df_Scale=df_cleaned.copy()
df_standardize=df_cleaned.copy()
selected_columns=["age","credit_sum","credit_month","score_shk","monthly_income","credit_count","overdue_credit_count","open_account_flg"]
#--------------------------------------------------------------------------------------------------
selected_data = df_standardize[selected_columns].copy()  
scaler = StandardScaler()
selected_data[selected_columns] = scaler.fit_transform(selected_data[selected_columns])
df_standardize[selected_columns] = selected_data #стандартизированные данные
#--------------------------------------------------------------------------------------------------
selected_data = df_Scale[selected_columns].copy() 
scaler = MinMaxScaler()
selected_data[selected_columns] = scaler.fit_transform(selected_data[selected_columns])
df_Scale[selected_columns] = selected_data #маштабированные данные



# X - признаки, y - метки ,признаки в этом коде взяты из отфильтрованного от пропусков датасета,но мо можем взять df_Scale или  df_standardize вместо него
X = df_cleaned.drop('open_account_flg', axis=1)  # убираем столбец с метками из признаков
y = df_cleaned['open_account_flg']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
"""
По итогу у нас получилось 3 вариации датасета  df_cleaned - очищенныей от пропусков
df_standardize - стандартизиррованные данные
df_Scale -маштабированные данные 
а также механизм разбиения на тестовую и обучающую выборку куда можно подставить любой вариант датасета
"""