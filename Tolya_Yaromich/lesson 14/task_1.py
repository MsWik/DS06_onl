import numpy as np

np.random.seed(42)

lr = 1
def mean_squared_error(y_true, y_pred):
    """
    Функция для вычисления среднеквадратичной ошибки.
    """
    return np.mean((y_true - y_pred) ** 2)

def gradient(y_true, y_pred, x):
    """
    Функция подсчета градиента среднеквадратичной ошибки.
    """
    n = len(y_true)
    grad = -2/n * np.dot(x.T, (y_true - y_pred))
    return grad

def update(alpha, gradient, lr):
    """
    Функция обновления весов с использованием градиентного спуска.
    """
    alpha_new = alpha - lr * gradient
    return alpha_new

def train(alpha0, x_train, y_train, lr, num_epoch):
    alpha = alpha0.copy()

    n = len(y_train)

    for epo in range(num_epoch):
        y_pred_all = np.dot(x_train, alpha)
        grad = gradient( y_train,y_pred_all,x_train)
        alpha = update(alpha, grad, lr)
        lr = lr * 0.95 
        mse = mean_squared_error(y_train, np.dot(x_train, alpha))
        print(f"Эпоха {epo + 1}/{num_epoch}, MSE: {mse}, Lr: {lr}")

    return alpha


x_train = 2 * np.random.rand(100, 1)
y_train = 4 + 3 * x_train + np.random.randn(100, 1)


x_train_b = np.c_[np.ones((100, 1)), x_train]


alpha0 = np.random.randn(2, 1)




num_epoch = 100


final_alpha = train(alpha0, x_train_b, y_train, lr, num_epoch)

print("Финальные веса:", final_alpha)
