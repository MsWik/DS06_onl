import tensorflow as tf
import pandas as pd
import numpy as np
from keras.layers import Dense, BatchNormalization, InputLayer, LeakyReLU, ReLU
from sklearn.utils import compute_class_weight

class Model:
    def __init__(
            self,
            x_train: tf.Tensor,
            y_train: tf.Tensor,
            x_val: tf.Tensor,
            y_val: tf.Tensor,
            epochs: int,
            learning_rate: float
            ) -> None:
        self.__x_train: tf.Tensor = x_train
        self.__y_train: tf.Tensor = tf.one_hot(y_train, depth=2)
        self.__x_val: tf.Tensor = x_val
        self.__y_val: tf.Tensor = tf.one_hot(y_val, depth=2)
        self.__epochs: int = epochs
        self.__learning_rate: float = learning_rate


    def __set_params(self) -> None:
        self.__class_labels = np.unique(np.argmax(self.__y_train, axis=1))
        self.__class_weights = compute_class_weight('balanced', classes=self.__class_labels,  y=np.argmax(self.__y_train, axis=1).reshape(-1))
        self.__class_weight_dict = {label: weight for label, weight in zip(self.__class_labels, self.__class_weights)} 


        self.__optimizer = tf.keras.optimizers.Adam(
            learning_rate=self.__learning_rate,
            epsilon=1e-6,
            amsgrad=True,
            use_ema=True,
        )
        self.__loss = tf.keras.losses.BinaryCrossentropy()
        self.__metric = tf.keras.metrics.AUC()


    def __create_model(self) -> None:
        self.__input_layer = InputLayer(10)

        x = Dense(units=256, activation=ReLU(), dtype=tf.float32)(self.__input_layer.output)
        x = BatchNormalization()(x)
        x = Dense(units=128, activation=ReLU(), dtype=tf.float32)(x)
        x = BatchNormalization()(x)
        x = Dense(units=64, activation=ReLU(), dtype=tf.float32)(x)
        x = BatchNormalization()(x)
        output = Dense(units=2, activation="softmax", dtype=tf.float32)(x)

        self.__model = tf.keras.models.Model(inputs = self.__input_layer.input, outputs = output)

        self.__model.compile(
            optimizer=self.__optimizer,
            loss=self.__loss,
            metrics=self.__metric,
        )


    def __train(self) -> None:
        self.__check_point = tf.keras.callbacks.ModelCheckpoint(
            'model_cp',
            monitor='val_auc',
            save_best_only=True,
            mode='max',
            initial_value_threshold=0.7,
            )
        
        self.__model.fit(
            self.__x_train,
            self.__y_train,
            batch_size=8192,
            epochs=self.__epochs,
            callbacks=self.__check_point,
            validation_data=(self.__x_val, self.__y_val),
            class_weight=self.__class_weight_dict,
        )
    
    
    def run(self) -> None:
        self.__set_params()
        self.__create_model()
        self.__train()


def main() -> None:
    train_data: pd.DataFrame = pd.read_csv('train_data.csv')
    val_data: pd.DataFrame = pd.read_csv('val_data.csv')
    y_train: tf.Tensor = tf.reshape(tf.convert_to_tensor(train_data.drop(train_data.columns[1:], axis=1), dtype=tf.uint8), shape=-1)
    x_train: tf.Tensor = tf.convert_to_tensor(train_data.drop(train_data.columns[:1], axis=1), dtype=tf.float32)
    y_val: tf.Tensor = tf.reshape(tf.convert_to_tensor(val_data.drop(val_data.columns[1:], axis=1), dtype=tf.uint8), shape=-1)
    x_val: tf.Tensor = tf.convert_to_tensor(val_data.drop(val_data.columns[:1], axis=1), dtype=tf.float32)
    model = Model(
        x_train=x_train,
        y_train=y_train,
        x_val=x_val,
        y_val=y_val,
        epochs=1000,
        learning_rate=0.0001,
    )
    model.run()



if __name__ == '__main__':
    for device in tf.config.list_physical_devices('GPU'):
        tf.config.experimental.set_memory_growth(device, enable=True)
    with tf.device('/device:GPU:0'):
        main()