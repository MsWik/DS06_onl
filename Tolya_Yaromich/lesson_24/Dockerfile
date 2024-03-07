FROM jupyter/datascience-notebook


#Установка бибилиотек
RUN pip install pandas numpy scikit-learn scipy mlxtend

# рабочий каталог
WORKDIR /app/

# Копируем Jupyter Notebook и датасет в контейнер
COPY task1.ipynb /app/
COPY dataset.csv /app/



