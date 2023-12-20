import numpy as np

np.random.seed(42)


# Функция подсчета градиента
def gradient(y_true: float, y_pred: float, x: np.array) -> np.array:
    grad = 2 * (y_pred - y_true) * x
    return grad


y_true = 5
y_pred = 4.5
x = np.array([3, 4, 5])

grad = gradient(y_true, y_pred, x)
print(grad)


# Функция обновления весов
def update(alpha: np.array, gradient: np.array, lr: float):
    """
    alpha: текущее приближения вектора параметров модели
    gradient: посчитанный градиент по параметрам модели
    lr: learning rate, множитель перед градиентом в формуле обновления параметров
    """
    alpha_new = alpha - lr * gradient
    return alpha_new


alpha = np.array([0.5, 0.5, 0.5])
grad = np.array([1.0, 2.0, 3.0])
lr = 0.1

alpha_new = update(alpha, grad, lr)
print(alpha_new)


# функция тренировки модели
def train(
        alpha0: np.array, x_train: np.array, y_train: np.array, lr: float, num_epoch: int
):
    """
    alpha0 - начальное приближение параметров модели
    x_train - матрица объект-признак обучающей выборки
    y_train - верные ответы для обучающей выборки
    lr - learning rate, множитель перед градиентом в формуле обновления параметров
    num_epoch - количество эпох обучения, то есть полных 'проходов' через весь датасет
    """
    alpha = alpha0.copy()
    for epo in range(num_epoch):
        for i, x in enumerate(x_train):
            y_pred = np.dot(x, alpha)
            grad = gradient(y_train[i], y_pred, x)
            alpha = update(alpha, grad, lr)
        return alpha


alpha0 = np.array([0.5, 0.5])
x_train = np.array([[1, 2], [2, 3], [3, 4]])
y_train = np.array([1, 2, 3])
lr = 0.01
num_epoch = 5

trained_alpha = train(alpha0, x_train, y_train, lr, num_epoch)
print(trained_alpha)
