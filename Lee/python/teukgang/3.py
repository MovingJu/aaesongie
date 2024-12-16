import os
import tensorflow as tf
import numpy as np
from sklearn.model_selection import KFold
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import GlobalAveragePooling2D

# 설정
size = 64

# 데이터 경로 설정
train_dir = './teukgang/Drug Addicted or Not People - DANP/train'
test_dir = './teukgang/Drug Addicted or Not People - DANP/test'

# 이미지 파일 경로와 라벨 리스트 생성
image_files = []
labels = []

# 클래스 디렉토리 탐색 (예시: 'class_0', 'class_1' 디렉토리가 있을 것)
for class_dir in os.listdir(train_dir):
    class_path = os.path.join(train_dir, class_dir)
    if os.path.isdir(class_path):
        for filename in os.listdir(class_path):
            image_path = os.path.join(class_path, filename)
            image_files.append(image_path)
            labels.append(class_dir)  # 클래스 디렉토리 이름을 라벨로 사용 (예: 'class_0' 또는 'class_1')

# 데이터가 5개의 fold로 나누기에 충분한지 확인
if len(image_files) < 5:
    raise ValueError(f"Cannot have number of splits n_splits={5} greater than the number of samples n_samples={len(image_files)}.")

# 데이터 전처리 및 증강
train_datagen = ImageDataGenerator(
    rescale=1./255,              # 정규화
    rotation_range=30,          # 이미지 회전
    width_shift_range=0.2,      # 좌우 이동
    height_shift_range=0.2,     # 상하 이동
    shear_range=0.2,            # 기울기
    zoom_range=0.2,             # 확대/축소
    horizontal_flip=True,       # 좌우 반전
    fill_mode='nearest'         # 채워질 영역
)

test_datagen = ImageDataGenerator(rescale=1./255)  # 정규화만

# VGG16 모델을 사용한 전이 학습
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(size, size, 3))

# 특성 추출을 위한 기본 모델
for layer in base_model.layers:
    layer.trainable = False

# 모델 정의 함수
def create_model():
    model = tf.keras.Sequential([
        base_model,
        GlobalAveragePooling2D(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# KFold 설정
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# K-fold 학습 및 평가
all_train_accuracies = []
all_val_accuracies = []

for fold, (train_idx, val_idx) in enumerate(kf.split(image_files), 1):
    print(f"Fold {fold}/{5}")

    # KFold 인덱스를 통해 트레인과 검증 데이터를 분할
    train_images = [image_files[i] for i in train_idx]
    val_images = [image_files[i] for i in val_idx]

    # 데이터 증강을 위한 제너레이터 설정
    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(size, size),
        batch_size=32,
        class_mode='binary',
        shuffle=True
    )

    val_generator = test_datagen.flow_from_directory(
        train_dir,
        target_size=(size, size),
        batch_size=32,
        class_mode='binary',
        shuffle=False
    )

    # 모델 생성
    model = create_model()

    # 콜백 설정
    early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=5)

    # 모델 학습
    history = model.fit(
        train_generator,
        epochs=100,
        validation_data=val_generator,
        callbacks=[early_stopping, reduce_lr]
    )

    # 평가
    val_acc = history.history['val_accuracy'][-1]
    all_val_accuracies.append(val_acc)
    
    print(f"Fold {fold} validation accuracy: {val_acc:.4f}")

# 평균 정확도 출력
avg_val_acc = np.mean(all_val_accuracies)
print(f"Average validation accuracy across {5} folds: {avg_val_acc:.4f}")

# 모델 저장 (선택 사항)
model.save('4.keras')
