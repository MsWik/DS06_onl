# Используем официальный образ Python как базовый образ
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в рабочую директорию
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir flask scikit-learn joblib catboost --upgrade-strategy eager

# Указываем порт, который будет слушать контейнер
EXPOSE 5000

# Копируем файл с обученной моделью
COPY cat_model.pkl /app/cat_model.pkl


# Запускаем приложение
CMD ["python", "app.py"]