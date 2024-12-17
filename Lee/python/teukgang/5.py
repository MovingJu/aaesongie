import os
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import GlobalAveragePooling2D, BatchNormalization, Conv2D, MaxPooling2D, Dropout
from sklearn.model_selection import KFold  # KFold 임포트

# 설정
size = 64

# 데이터 경로 설정
train_dir = './teukgang/danp/train'
test_dir = './teukgang/danp/test'

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
    rotation_range=40,          # 이미지 회전 강도 증가
    width_shift_range=0.3,      # 좌우 이동 범위 증가
    height_shift_range=0.3,     # 상하 이동 범위 증가
    shear_range=0.3,            # 기울기
    zoom_range=0.3,             # 확대/축소 범위 증가
    horizontal_flip=True,       # 좌우 반전
    fill_mode='nearest'         # 채워질 영역
)

test_datagen = ImageDataGenerator(rescale=1./255)  # 정규화만


# 모델 정의 함수 (개선된 모델)
def create_model():
    model = models.Sequential([
        # 첫 번째 합성곱 + 풀링 레이어
        layers.Conv2D(64, (3, 3), activation='relu', input_shape=(128, 128, 3), padding='same'),
        layers.MaxPooling2D(pool_size=(2, 2), padding='valid'),

        # 두 번째 합성곱 + 풀링 레이어
        layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D(pool_size=(2, 2), padding='valid'),

        # 세 번째 합성곱 + 풀링 레이어
        layers.Conv2D(256, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D(pool_size=(2, 2), padding='valid'),

        # 네 번째 합성곱 + 풀링 레이어
        layers.Conv2D(512, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D(pool_size=(2, 2), padding='valid'),

        # 특성 맵을 1D 벡터로 변환
        layers.Flatten(),

        # 전결합(Dense) 레이어
        layers.Dense(4096, activation='relu'),
        layers.Dropout(0.5),  # 과적합 방지

        # 출력 레이어 (이진 분류 예시)
        layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    return model

# K-fold 설정
kf = KFold(n_splits=2, shuffle=True, random_state=42)

# K-fold 학습
for fold, (train_idx, val_idx) in enumerate(kf.split(image_files), 1):
    print(f"Fold {fold}/{5}")

    # 데이터 증강을 위한 제너레이터 설정
    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(size, size),
        batch_size=32,
        class_mode='binary',
        shuffle=True
    )

    val_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(size, size),
        batch_size=32,
        class_mode='binary',
        shuffle=False
    )

    # 모델 생성
    model = create_model()

    # 콜백 설정
    # early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
    # reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=5)

    # 모델 학습
    history = model.fit(
        train_generator,
        epochs=100,
        validation_data=val_generator,
        # callbacks=[early_stopping, reduce_lr]
    )

# 최종 테스트 데이터 평가
test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(size, size),  # 모델의 입력 크기에 맞게 설정
    batch_size=32,
    class_mode='binary',  # 이진 분류로 설정
    shuffle=False  # 평가 시 순서가 중요하므로 shuffle=False로 설정
)

# 모델 평가 (테스트 데이터에 대한 정확도)
test_loss, test_acc = model.evaluate(test_generator)
print(f"Final test accuracy: {test_acc:.4f}")

# 모델 저장 (선택 사항)
model.save('5.keras')
