import tensorflow as tf
import PIL.Image
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import load_img, img_to_array
import os

# 데이터 경로 설정
train_dir = './teukgang/Drug Addicted or Not People - DANP/train'
test_dir = './teukgang/Drug Addicted or Not People - DANP/test'

def predict_image(image_path):
    img = load_img(image_path, target_size=(128, 128))  # 이미지 크기 조정
    img_array = img_to_array(img) / 255.0  # 정규화
    img_array = tf.expand_dims(img_array, axis=0)  # 배치 차원 추가
    prediction = loaded_model.predict(img_array)
    print(f"이미지 '{image_path}'의 중독 확률: {prediction[0][0]:.4f}")


loaded_model = tf.keras.models.load_model('image_classification_model.h5')

for i in range(1, 41, 1):
    predict_image(f'./teukgang/Drug Addicted or Not People - DANP/test/Not Addicted/{i}.png')
    predict_image(f'./teukgang/Drug Addicted or Not People - DANP/test/Addicted/{i}.png')