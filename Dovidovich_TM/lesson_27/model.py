import tensorflow as tf
import numpy as np
from keras.layers import Dense, Conv2D, InputLayer, LeakyReLU, MaxPooling2D, Add, GlobalAveragePooling2D, BatchNormalization
from keras.models import Model
from keras.optimizers import Adam
from keras.losses import CategoricalCrossentropy
from keras.metrics import CategoricalAccuracy, F1Score
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.initializers import he_normal
from keras.regularizers import L2
from sklearn.utils import compute_class_weight
from typing import Sequence


class IModel:
    def __init__(
        self,
        x_train: tf.Tensor,
        y_train: tf.Tensor,
        x_test: tf.Tensor,
        y_test: tf.Tensor,
        x_val: tf.Tensor,
        y_val: tf.Tensor,
        *,
        learning_rate: float,
        epochs: int,
    ) -> None:
        self.__x_train: tf.Tensor = x_train
        self.__y_train: tf.Tensor = tf.one_hot(y_train, depth=6)
        self.__x_test: tf.Tensor = x_test
        self.__y_test: tf.Tensor = tf.one_hot(y_test, depth=6)
        self.__x_val: tf.Tensor = x_val
        self.__y_val: tf.Tensor = tf.one_hot(y_val, depth=6)
        self.__learning_rate: float = learning_rate
        self.__epochs: int = epochs

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
        self.__metrics = [CategoricalAccuracy(), F1Score(average='macro')]

    def __create_conv_block(
        self,
        inputs,
        filters: int,
        kernel_size: Sequence,
        strides: Sequence = (1, 1),
    ) -> None:
        x = Conv2D(filters=filters, kernel_size=kernel_size, strides=strides, padding='same',
                   activation=LeakyReLU(), kernel_initializer=he_normal(seed=42), kernel_regularizer=L2())(inputs)
        x = BatchNormalization()(x)
        return x

    def __create_res_block(
        self,
        inputs,
        filters: int
    ):
        x = self.__create_conv_block(inputs, filters, kernel_size=(3, 3))
        x = self.__create_conv_block(x, filters, kernel_size=(3, 3))
        x = Add()([x, inputs])
        return x

    def __create_model(self) -> None:

        self.__input_layer = InputLayer(input_shape=(150, 150, 3))
        x = self.__create_conv_block(
            self.__input_layer.output, filters=64, kernel_size=(7, 7), strides=(2, 2))
        x = MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding='same')(x)
        for _ in range(3):
            x = self.__create_res_block(x, 64)
        x = self.__create_conv_block(
            x, filters=128, kernel_size=(3, 3), strides=(2, 2))
        for _ in range(3):
            x = self.__create_res_block(x, 128)
        # -----------------------------------------------------
        x = self.__create_conv_block(
            x, filters=256, kernel_size=(3, 3), strides=(2, 2))
        for _ in range(5):
            x = self.__create_res_block(x, 256)
        x = self.__create_conv_block(
            x, filters=512, kernel_size=(3, 3), strides=(2, 2))
        for _ in range(2):
            x = self.__create_res_block(x, 512)
        # -----------------------------------------------------
        # ↑↑↑↑↑ Если удалить эти строки, то получится модель чуть попроще(в выводе написал)
        x = GlobalAveragePooling2D()(x)
        output = Dense(6, activation='softmax')(x)

        self.__model: Model = Model(
            inputs=self.__input_layer.input,
            outputs=output,
        )
        self.__model.compile(
            optimizer=self.__optimizer,
            loss=self.__loss,
            metrics=self.__metrics,
        )

    def __train(self) -> None:
        self.__check_point = ModelCheckpoint(
            'model',
            monitor='val_f1_score',
            save_best_only=True,
            mode='max',
            initial_value_threshold=0.7,
        )
        self.__early_stopping = EarlyStopping(
            monitor='val_f1_score',
            patience=10,
            start_from_epoch=50,
        )
        self.__model.fit(
            self.__x_train,
            self.__y_train,
            batch_size=64,
            epochs=self.__epochs,
            callbacks=[
                self.__check_point,
                self.__early_stopping,
            ],
            validation_data=(self.__x_val, self.__y_val),
            class_weight=self.__class_weight_dict,
        )

    def __test(self) -> None:
        self.__model.evaluate(self.__x_test, self.__y_test, batch_size=32)

    def run(self) -> None:
        self.__set_params()
        self.__create_model()
        self.__train()
        self.__test()


def main() -> None:
    x_train: tf.Tensor = tf.convert_to_tensor(np.load('x_train.npy'))
    y_train: tf.Tensor = tf.convert_to_tensor(np.load('y_train.npy'))
    x_test: tf.Tensor = tf.convert_to_tensor(np.load('x_test.npy'))
    y_test: tf.Tensor = tf.convert_to_tensor(np.load('y_test.npy'))
    x_val: tf.Tensor = tf.convert_to_tensor(np.load('x_val.npy'))
    y_val: tf.Tensor = tf.convert_to_tensor(np.load('y_val.npy'))
    model = IModel(
        x_train,
        y_train,
        x_test,
        y_test,
        x_val,
        y_val,
        learning_rate=0.0005,
        epochs=1000,
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
