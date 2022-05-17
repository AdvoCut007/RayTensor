import keras
import numpy as np
import tensorflow as tf
from keras import layers
from keras import Sequential


class RayTensor:
    def __init__(self):
        self.epochs = 5
        self.batch_size = 32
        self.img_height = 224
        self.img_width = 224
        self.train_path = 'CT/train/'
        self.val_path = 'CT/test/'
        self.xray_class_names = [
            'COVID19',
            'NORMAL',
            'PNEUMONIA',
            'TURBERCULOSIS'
        ]
        self.ct_class_names = [
            'COVID',
            'NORMAL',
            'PNEUMONIA'
        ]

    def xray_model_create(self):
        train_ds = tf.keras.utils.image_dataset_from_directory(
            self.train_path,
            validation_split=0.1,
            subset="training",
            seed=123,
            image_size=(self.img_height, self.img_width),
            batch_size=self.batch_size
        )

        val_ds = tf.keras.utils.image_dataset_from_directory(
            self.val_path,
            validation_split=0.9,
            subset="validation",
            seed=123,
            image_size=(self.img_height, self.img_width),
            batch_size=self.batch_size
        )

        class_names = train_ds.class_names

        layers.Rescaling(1. / 255)

        data_augmentation = keras.Sequential(
            [
                layers.RandomFlip("horizontal",
                                  input_shape=(self.img_height,
                                               self.img_width,
                                               3)
                                  ),
                layers.RandomRotation(0.1),
                layers.RandomZoom(0.1),
            ]
        )

        model = Sequential([
            data_augmentation,
            layers.Rescaling(1. / 255),
            layers.Conv2D(16, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(32, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(64, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Dropout(0.2),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dense(len(class_names))
        ])

        model.compile(optimizer='adam',
                      loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                      metrics=['accuracy'])

        model.fit(
            train_ds,
            validation_data=val_ds,
            epochs=self.epochs
        )

        model.save('xray_model.h5')

    def xray_predict(self, path_to_image):
        model = keras.models.load_model('xray_model.h5')
        img = tf.keras.utils.load_img(
            path_to_image, target_size=(
                self.img_height,
                self.img_width
            )
        )

        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])

        if self.xray_class_names[np.argmax(score)] == 'PNEUMONIA':
            self.xray_class_names[np.argmax(score)] = 'пневмония'
        elif self.xray_class_names[np.argmax(score)] == 'NORMAL':
            self.xray_class_names[np.argmax(score)] = 'всё хорошо'
        elif self.xray_class_names[np.argmax(score)] == 'COVID19':
            self.xray_class_names[np.argmax(score)] = 'Covid-19'
        elif self.xray_class_names[np.argmax(score)] == 'TURBERCULOSIS':
            self.xray_class_names[np.argmax(score)] = 'туберкулёз'

        return [
            self.xray_class_names,
            np.array(score * 100),
            100 * np.max(score),
            self.xray_class_names[np.argmax(score)]
        ]

    def ct_model_create(self):
        train_ds = tf.keras.utils.image_dataset_from_directory(
            self.train_path,
            validation_split=0.2,
            subset="training",
            seed=123,
            image_size=(self.img_height, self.img_width),
            batch_size=self.batch_size
        )

        val_ds = tf.keras.utils.image_dataset_from_directory(
            self.val_path,
            validation_split=0.2,
            subset="validation",
            seed=123,
            image_size=(self.img_height, self.img_width),
            batch_size=self.batch_size
        )

        class_names = train_ds.class_names

        layers.Rescaling(1. / 255)

        data_augmentation = keras.Sequential(
            [
                layers.RandomFlip("horizontal",
                                  input_shape=(self.img_height,
                                               self.img_width,
                                               3)
                                  ),
                layers.RandomRotation(0.1),
                layers.RandomZoom(0.1),
            ]
        )

        model = Sequential([
            data_augmentation,
            layers.Rescaling(1. / 255),
            layers.Conv2D(16, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(32, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(64, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Dropout(0.2),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dense(len(class_names))
        ])

        model.compile(optimizer='adam',
                      loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                      metrics=['accuracy'])

        model.fit(
            train_ds,
            validation_data=val_ds,
            epochs=self.epochs
        )

        model.save('ct_model.h5')

    def ct_predict(self, path_to_image):
        model = keras.models.load_model('ct_model.h5')
        img = tf.keras.utils.load_img(
            path_to_image, target_size=(
                self.img_height,
                self.img_width
            )
        )

        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])

        if self.ct_class_names[np.argmax(score)] == 'PNEUMONIA':
            self.ct_class_names[np.argmax(score)] = 'пневмония'
        elif self.ct_class_names[np.argmax(score)] == 'NORMAL':
            self.ct_class_names[np.argmax(score)] = 'всё хорошо'
        elif self.ct_class_names[np.argmax(score)] == 'COVID19':
            self.ct_class_names[np.argmax(score)] = 'Covid-19'

        return [
            self.ct_class_names,
            np.array(score * 100),
            100 * np.max(score),
            self.ct_class_names[np.argmax(score)]
        ]
