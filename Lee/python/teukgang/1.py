import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
import numpy as np
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import img_to_array, load_img
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import GlobalAveragePooling2D
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau

# 데이터 경로 설정
train_dir = './teukgang/Drug Addicted or Not People - DANP/train'
test_dir = './teukgang/Drug Addicted or Not People - DANP/test'


size = 64


# 데이터 전처리 및 증강
train_datagen = ImageDataGenerator(
    rescale=1./255
)

test_datagen = ImageDataGenerator(rescale=1./255)  # 정규화만

# 데이터 로드
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(size, size),  # 이미지 크기 조정
    batch_size=32,
    class_mode='binary'        # 이진 분류로 설정
)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(size, size),
    batch_size=32,
    class_mode='binary'
)

# VGG16 모델을 사용한 전이 학습
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(size, size, 3))

# 특성 추출을 위한 기본 모델
for layer in base_model.layers:
    layer.trainable = False

# 모델 정의
model = tf.keras.Sequential([
    base_model,
    GlobalAveragePooling2D(),

    tf.keras.layers.Dense(30, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(30, activation='relu'),
    tf.keras.layers.Dropout(0.5),

    tf.keras.layers.Dense(1, activation='sigmoid')

])

# 모델 컴파일
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 조기 종료 및 학습률 감소 설정
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=5)

# 모델 학습
model.fit(
    train_generator,
    epochs=10,
    validation_data=test_generator,
    callbacks=[early_stopping, reduce_lr]
)

# 테스트 데이터로 평가
test_loss, test_acc = model.evaluate(test_generator)
print(f"테스트 정확도: {test_acc:.4f}")

# 모델 저장 (선택 사항)
model.save('1.keras')
