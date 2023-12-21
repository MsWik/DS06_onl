import numpy as np


class KNN_classifier:
    def __init__(self, n_neighbors: int, **kwargs):
        self.K = n_neighbors

    def fit(self, x: np.array, y: np.array):
        self.x_train = x
        self.y_train = y
        #сохраняются обучающие данные

    def predict(self, x: np.array):
        predictions = []

        # Вычисляется расстояние от тестовых до обучающих образцов
        distances = pairwise_distances(x, self.x_train)

        # Для каждого тестового образца находим K ближайших соседей и их метки
        for i in range(distances.shape[0]):
            k_indices = np.argsort(distances[i])[:self.K]
            k_nearest_labels = self.y_train[k_indices]

            # Прогноз наиболее частой метки среди ближайших соседей
            prediction = mode(k_nearest_labels).mode[0]
            predictions.append(prediction)

        return np.array(predictions)
