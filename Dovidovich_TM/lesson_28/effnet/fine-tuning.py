import numpy as np
import tensorflow as tf
from keras.losses import CategoricalCrossentropy
from keras.metrics import F1Score, CategoricalAccuracy
from keras.optimizers import Adam
from keras.models import load_model, Model
from keras.callbacks import EarlyStopping, ModelCheckpoint
# from keras.preprocessing.image import ImageDataGenerator
from sklearn.utils import compute_class_weight

class ImageModel:
    def __init__(
            self,
            x_train: tf.Tensor,
            y_train: tf.Tensor,
            x_test: tf.Tensor,
            y_test: tf.Tensor,
            x_valid: tf.Tensor,
            y_valid: tf.Tensor,
            *,
            learning_rate: float,
            epochs: int,
            ) -> None:
        self.__x_train: tf.Tensor = x_train
        self.__y_train: tf.Tensor = tf.one_hot(y_train, depth=53)
        self.__x_test: tf.Tensor = x_test
        self.__y_test: tf.Tensor = tf.one_hot(y_test, depth=53)
        self.__x_valid: tf.Tensor = x_valid
        self.__y_valid: tf.Tensor = tf.one_hot(y_valid, depth=53)
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
            beta_2=0.98,
            epsilon=1e-6,
            amsgrad=True,
            weight_decay=0.1,
            use_ema=True,
        )
        self.__loss = CategoricalCrossentropy()
        self.__metrics = [
            F1Score(average='macro'),
            CategoricalAccuracy(),
            ]


    def __load_model(self) -> None:
        self.__model: Model = load_model('model')
        for layer in self.__model.layers:
            layer.trainable = True

        self.__model.compile(
            optimizer=self.__optimizer,
            loss=self.__loss,
            metrics=self.__metrics
        )

    def __train(self) -> None:
        self.__checkpoint = ModelCheckpoint(
            'model_fine_tuned',
            monitor='val_f1_score',
            save_best_only=True,
            mode='max',
            initial_value_threshold=0.9,
        ) 

        self.__early_stopping = EarlyStopping(
            monitor='val_f1_score',
            min_delta=0.02,
            patience=30,
            start_from_epoch=50,
        )

        self.__model.fit(
            self.__x_train,
            self.__y_train,
            batch_size=16,
            epochs=self.__epochs,
            callbacks=[
                self.__checkpoint,
                self.__early_stopping,
            ],
            validation_data=(self.__x_valid, self.__y_valid),
            class_weight=self.__class_weight_dict,
            validation_batch_size=16,
        )


    def __test(self) -> None:
        self.__model.evaluate(self.__x_test, self.__y_test, batch_size=32)

    def run(self) -> None:
        self.__set_params()
        self.__load_model()
        self.__train()
        self.__test()

def main() -> None:
    x_train: tf.Tensor = tf.convert_to_tensor(np.load('../x_train.npy'))
    y_train: tf.Tensor = tf.convert_to_tensor(np.load('../y_train.npy'))
    x_test: tf.Tensor = tf.convert_to_tensor(np.load('../x_test.npy'))
    y_test: tf.Tensor = tf.convert_to_tensor(np.load('../y_test.npy'))
    x_valid: tf.Tensor = tf.convert_to_tensor(np.load('../x_valid.npy'))
    y_valid: tf.Tensor = tf.convert_to_tensor(np.load('../y_valid.npy'))
    model = ImageModel(
        x_train,
        y_train,
        x_test,
        y_test,
        x_valid,
        y_valid,
        learning_rate=0.000005,
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