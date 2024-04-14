import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import Model
from keras.optimizers import Adam
from keras.activations import softmax
from keras.initializers import he_normal
from keras.losses import CategoricalCrossentropy
from keras.metrics import CategoricalAccuracy, F1Score
from keras.layers import Dense, LSTM, Input, Embedding, LeakyReLU, BatchNormalization, Concatenate, Bidirectional
from keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau, TerminateOnNaN, CSVLogger
from sklearn.utils import compute_class_weight


class TextModel:
    def __init__(
            self,
            x_train: tf.Tensor,
            x_train_classes: tf.Tensor,
            y_train: tf.Tensor, 
            x_test: tf.Tensor,
            x_test_classes: tf.Tensor, 
            y_test: tf.Tensor,
            x_valid: tf.Tensor,
            x_valid_classes: tf.Tensor, 
            y_valid: tf.Tensor,
            learning_rate: float,
            epochs: int
            ) -> None:
        self.__x_train: tf.Tensor = x_train
        self.__x_train_classes: tf.Tensor = tf.one_hot(x_train_classes, depth=32)
        self.__y_train: tf.Tensor = tf.one_hot(y_train, depth=4)
        self.__x_test: tf.Tensor = x_test
        self.__x_test_classes: tf.Tensor = tf.one_hot(x_test_classes, depth=32)
        self.__y_test: tf.Tensor = tf.one_hot(y_test, depth=4)
        self.__x_valid: tf.Tensor = x_valid
        self.__x_valid_classes: tf.Tensor = tf.one_hot(x_valid_classes, depth=32)
        self.__y_valid: tf.Tensor = tf.one_hot(y_valid, depth=4)
        self.__learning_rate: float = learning_rate
        self.__epochs = epochs

    def __set_params(self) -> None:
        self.__class_labels = np.unique(np.argmax(self.__y_train, axis=1))
        self.__class_weights = compute_class_weight(
            'balanced', classes=self.__class_labels,  y=np.argmax(self.__y_train, axis=1).reshape(-1))
        self.__class_weight_dict = {label: weight for label, weight in zip(
            self.__class_labels, self.__class_weights)}
        
        self.__optimizer = Adam(
            learning_rate=self.__learning_rate,
            epsilon=1e-6,
            amsgrad=True,
            use_ema=True,
        )

        self.__loss = CategoricalCrossentropy()
        self.__metrics = [
            CategoricalAccuracy(name='accuracy'),
            F1Score(average='macro', name='f1score')
        ]

    def __create_model(self) -> None:
        self.__input_1 = Input(shape=(32,), name='game_class', dtype=tf.float32) # для класса игры-компании
        self.__input_2 = Input(shape=(128,), name='sequence', dtype=tf.float32) # для последовательности(вектора)

        x = Embedding(input_dim=128, output_dim=256)(self.__input_2)
        x = Bidirectional(LSTM(units=256, return_sequences=True, dtype=tf.float32))(x)
        x = BatchNormalization()(x)
        x = Bidirectional(LSTM(units=128, return_sequences=True, dtype=tf.float32))(x)
        x = BatchNormalization()(x)
        x = Bidirectional(LSTM(units=64, return_sequences=False, dtype=tf.float32))(x)
        x = Dense(units=64, activation=LeakyReLU(), kernel_initializer=he_normal(seed=23), dtype=tf.float32)(x)

        y = Dense(units=16, activation=LeakyReLU(), kernel_initializer=he_normal(seed=23), dtype=tf.float32)(self.__input_1)
        
        z = Concatenate()([x, y])
        
        output = Dense(units=4, activation=softmax)(z)

        self.__model: Model = Model([self.__input_1, self.__input_2], output)

        self.__model.compile(
            optimizer=self.__optimizer,
            loss = self.__loss,
            metrics = self.__metrics,
        )
        self.__model.summary(line_length=196)


    def __train(self) -> None:
        self.__checkpoint = ModelCheckpoint(
            'model.keras',
            monitor='val_f1score',
            save_best_only=True,
            mode='max',
            initial_value_threshold=0.6,
        )

        self.__early_stopping = EarlyStopping(
            monitor='val_f1score',
            min_delta=0.01,
            patience=10,
            start_from_epoch=20,
        )

        self.__logger = CSVLogger('logs')
        
        self.__reducer = ReduceLROnPlateau(
            monitor='val_f1score',
            factor=0.1,
            patience=15,
            mode='max',
            min_delta=0.01,
            cooldown=5,
            min_lr=5e-6,
        )

        self.__nan_termination = TerminateOnNaN()

        print(self.__x_train_classes.shape, self.__x_train.shape, self.__y_train.shape)
        
        self.__model.fit(
            [self.__x_train_classes, self.__x_train],
            self.__y_train,
            batch_size=512,
            epochs=self.__epochs,
            callbacks=[
                self.__checkpoint,
                self.__early_stopping,
                self.__logger,
                self.__reducer,
                self.__nan_termination,
            ],
            validation_data=[[self.__x_valid_classes, self.__x_valid], self.__y_valid],
            class_weight=self.__class_weight_dict,
        )

    def __test(self) -> None:
        self.__model.evaluate(
            [self.__x_test_classes, self.__x_test],
            self.__y_test,
            batch_size=16,
        )

    def run(self) -> None:
        self.__set_params()
        self.__create_model()
        self.__train()
        self.__test()


def main() -> None:
    train_data = pd.read_csv('training_cleared.csv')
    test_data = pd.read_csv('test_cleared.csv')
    valid_data = pd.read_csv('valid_cleared.csv')

    y_train = tf.convert_to_tensor(train_data.flag)
    y_test = tf.convert_to_tensor(test_data.flag)
    x_train_classes = tf.convert_to_tensor(train_data.game_name)
    x_test_classes = tf.convert_to_tensor(test_data.game_name)
    x_train = tf.convert_to_tensor(np.load('train.npy'), dtype=tf.float32)
    x_test = tf.convert_to_tensor(np.load('test.npy'), dtype=tf.float32)
    y_valid = tf.convert_to_tensor(valid_data.flag)
    x_valid_classes = tf.convert_to_tensor(valid_data.game_name)
    x_valid = tf.convert_to_tensor(np.load('valid.npy'), dtype=tf.float32)



    model = TextModel(
        x_train,
        x_train_classes,
        y_train,
        x_test,
        x_test_classes,
        y_test,
        x_valid,
        x_valid_classes,
        y_valid,
        1e-4,
        1000,
    )
    model.run()

if __name__ == '__main__':
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        tf.config.set_logical_device_configuration(
            gpus[0],
            [tf.config.LogicalDeviceConfiguration(memory_limit=6144)]
        )
    with tf.device("/device:GPU:0"):
        main()