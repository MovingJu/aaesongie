import tensorflow as tf
import os
import numpy as np
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import KFold
from tensorflow.keras.utils import img_to_array, load_img

size = 128

# 데이터 경로 설정
train_dir = './teukgang/Drug Addicted or Not People - DANP/train'

# 데이터 전처리 및 증강
train_datagen = ImageDataGenerator(rescale=1./255)

# 데이터를 파일로부터 로드하는 함수 정의
def load_images_from_directory(directory):
    images = []
    labels = []
    class_names = os.listdir(directory)
    for label, class_name in enumerate(class_names):
        class_dir = os.path.join(directory, class_name)
        for filename in os.listdir(class_dir):
            img_path = os.path.join(class_dir, filename)
            img = load_img(img_path, target_size=(size, size))
            img_array = img_to_array(img) / 255.0
            images.append(img_array)
            labels.append(label)
    return np.array(images), np.array(labels)

# 데이터 로드
X, y = load_images_from_directory(train_dir)

# K-fold 설정
kfold = KFold(n_splits=3, shuffle=True, random_state=42)

fold_no = 1
for train_idx, val_idx in kfold.split(X, y):
    print(f"Training fold {fold_no}...")

    # 훈련 데이터 및 검증 데이터 분리
    X_train, X_val = X[train_idx], X[val_idx]
    y_train, y_val = y[train_idx], y[val_idx]

    # 모델 정의
    # model = models.Sequential([
    #     layers.Input(shape=(size, size, 3)),  # 이미지 크기에 맞는 입력층
    #     layers.Conv2D(32, (3, 3), activation='relu'),
    #     layers.MaxPooling2D((2, 2)),
    #     layers.Conv2D(64, (3, 3), activation='relu'),
    #     layers.MaxPooling2D((2, 2)),
    #     layers.Flatten(),
    #     layers.Dense(128, activation='relu'),
    #     layers.Dense(1, activation='sigmoid')  # 이진 분류를 위한 출력층
    # ])

    model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), padding="same", activation="relu", input_shape=(size, size, 3)),
    # tf.keras.layers.Input(shape=(size, size, 3)),  # 이미지 크기에 맞는 입력층 (128x128x3)
    tf.keras.layers.Flatten(),  # 3D 이미지를 1D 벡터로 변환
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(128, activation="relu"),


    tf.keras.layers.Dense(1, activation="sigmoid"),  # 이진 분류를 위한 출력층
])

    # 모델 컴파일
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    # 모델 학습
    model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val), batch_size=32)

    # 검증 데이터로 평가
    val_loss, val_acc = model.evaluate(X_val, y_val)
    print(f"Fold {fold_no} Validation Accuracy: {val_acc:.4f}")

    fold_no += 1


model.summary()


# 전체 테스트 데이터로 모델 평가 (선택 사항)
test_dir = './teukgang/Drug Addicted or Not People - DANP/test'
test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(size, size),
    batch_size=32,
    class_mode='binary'
)

test_loss, test_acc = model.evaluate(test_generator)
print(f"전체 테스트 정확도: {test_acc:.4f}")

# 모델 저장 (선택 사항)
model.save('image_classification_model.h5')

# 예측 함수 정의 (임의의 이미지에 대해 중독 확률 예측)
def predict_image(image_path):
    img = load_img(image_path, target_size=(size, size))  # 이미지 크기 조정
    img_array = img_to_array(img) / 255.0  # 정규화
    img_array = tf.expand_dims(img_array, axis=0)  # 배치 차원 추가
    prediction = model.predict(img_array)
    print(f"이미지 '{image_path}'의 중독 확률: {prediction[0][0]:.4f}")

# 예제 이미지 예측
predict_image('./teukgang/Drug Addicted or Not People - DANP/test/Not Addicted/1.png')
predict_image('./teukgang/Drug Addicted or Not People - DANP/test/Addicted/1.png')