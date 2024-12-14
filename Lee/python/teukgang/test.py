import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
from tensorflow.python.keras.models import load_model

def make_model():
    model = Sequential()
    
    # layer 1
    model.add(Conv2D(32, (3, 3), padding='same', input_shape=(32, 32, 3), activation='relu'))
    model.add(BatchNormalization())
    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))

    # layer 2
    model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    model.add(BatchNormalization())
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.3))

    # layer 3
    model.add(Conv2D(128, (3, 3), padding='same', activation='relu'))
    model.add(BatchNormalization())
    model.add(Conv2D(128, (3, 3), padding='same', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.4))

    # layer 4
    model.add(Conv2D(256, (3, 3), padding='same', activation='relu'))
    model.add(BatchNormalization())
    model.add(Conv2D(256, (3, 3), padding='same' ,activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.4))

    # layer 5
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.4))
    model.add(Dense(10, activation='softmax'))

    model.summary()

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    return model


def train(model, x ,y):
    x = x / 255.
    y = tf.keras.utils.to_categorical(y, 10)
    history = model.fit(x, y, epochs=MY_EPOCH, batch_size=MY_BATCH)
    model.save(filename)

    return history


def test(x, y):
    model = load_model(filename)
    x = x / 255.
    y = tf.keras.utils.to_categorical(y, 10)
    test_loss, test_acc = model.evaluate(x, y)
    
    return test_loss, test_acc


if __name__ == '__main__':
    (train_img, train_label), (test_img, test_label) = cifar10.load_data()

    # hyper parameters
    MY_EPOCH = 64
    MY_BATCH = 100
    filename = f'cifar_cnn_E({MY_EPOCH}).h5'

    cifar_cnn = make_model()

    # train
    train(cifar_cnn, train_img, train_label)

    # test
    loss, acc = test(test_img, test_label)

    print(f'"{filename}" 모델의 정확도 : {round(100 * acc, 2)}%')