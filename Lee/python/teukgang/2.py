import os
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import load_img, img_to_array

size = 128

# 데이터 경로 설정
train_dir = './teukgang/Drug Addicted or Not People - DANP/train'
test_dir = './teukgang/Drug Addicted or Not People - DANP/test'

# 데이터 전처리 및 증강
train_datagen = ImageDataGenerator(rescale=1./255)  # 정규화 추가
test_datagen = ImageDataGenerator(rescale=1./255)   # 정규화 추가


# 데이터 로드
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(size, size),  # 이미지 크기 조정
    batch_size=32,
    class_mode='binary'   # 이진 분류로 설정
)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(size, size),
    batch_size=32,
    class_mode='binary'
)

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


# 모델 정의
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), padding="same", activation="relu", input_shape=(size, size, 3)),
    # tf.keras.layers.Input(shape=(size, size, 3)),  # 이미지 크기에 맞는 입력층 (128x128x3)
    tf.keras.layers.Flatten(),  # 3D 이미지를 1D 벡터로 변환
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(128, activation="relu"),


    tf.keras.layers.Dense(1, activation="sigmoid"),  # 이진 분류를 위한 출력층
])

model.summary()

# 모델 컴파일
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 모델 학습
model.fit(
    train_generator,
    epochs=10,
    validation_data=test_generator
)

# 테스트 데이터로 평가
test_loss, test_acc = model.evaluate(test_generator)
print(f"테스트 정확도: {test_acc:.4f}")

# 모델 저장 (선택 사항)
model.save('image_classification_model.h5')

# 저장된 모델 불러오기 (선택 사항)
# loaded_model = tf.keras.models.load_model('image_classification_model.h5')

# 임의의 이미지에 대해 중독 확률 예측
def predict_image(image_path):
    img = load_img(image_path, target_size=(size, size))  # 이미지 크기 조정
    img_array = img_to_array(img)  # 정규화 없이 배열로 변환
    img_array = tf.expand_dims(img_array, axis=0)  # 배치 차원 추가
    prediction = model.predict(img_array)
    
    # 확률 출력
    prob = prediction[0][0]
    print(f"이미지 '{image_path}'의 중독 확률: {prob:.4f}")


# 예제 이미지 예측
predict_image('./teukgang/Drug Addicted or Not People - DANP/test/Not Addicted/1.png')
predict_image('./teukgang/Drug Addicted or Not People - DANP/test/Addicted/1.png')