import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 데이터 경로 설정
train_dir = './teukgang/Drug Addicted or Not People - DANP/train'
test_dir = './teukgang/Drug Addicted or Not People - DANP/test'

def predict_image(image_path):
    # 이미지 로드 및 전처리
    img = load_img(image_path, target_size=(64, 64))  # 이미지 크기 조정
    img_array = img_to_array(img) / 255.0  # 정규화
    img_array = tf.expand_dims(img_array, axis=0)  # 배치 차원 추가
    
    # 예측
    prediction = loaded_model.predict(img_array)
    
    # 중독 확률 계산 (1 - 예측 값)
    addicted_probability = 1 - prediction[0][0]
    
    # 예측 결과 출력
    result = "Addicted" if addicted_probability > 0.5 else "Not Addicted"
    return round(addicted_probability, 4), result

# 모델 불러오기
x = int(input('Enter the model number to load: '))
loaded_model = tf.keras.models.load_model(f'{x}.keras')

# 데이터 전처리
test_datagen = ImageDataGenerator(rescale=1./255)  # 정규화만

# 테스트 데이터 로드
test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(64, 64),  # 모델의 입력 크기에 맞게 설정
    batch_size=32,
    class_mode='binary',  # 이진 분류로 설정
    shuffle=False  # 평가 시 순서가 중요하므로 shuffle=False로 설정
)

# 모델 평가 (테스트 데이터에 대한 정확도)
test_loss, test_acc = loaded_model.evaluate(test_generator)

# 테스트 정확도 출력
print(f"Test accuracy: {test_acc:.4f}")

# 예시 이미지 예측 (개별 이미지)
print("Final test result for the input image:")
addicted_prob, result = predict_image('./teukgang/1.jpeg')
print(f"Predicted probability of addiction: {addicted_prob}, Result: {result}")

# 최종 점수 계산 (모델 정확도와 예측 결과를 반영한 점수)
final_score = round((test_acc * (1 - addicted_prob) * 100), 4)
print(f"Your score: {final_score}")

# # 추가적으로 여러 이미지에 대한 예측을 수행하는 코드:
# for i in range(1, 41):  # 예시: 1번부터 40번까지
#     image_path_not_addicted = f'./teukgang/Drug Addicted or Not People - DANP/test/Not Addicted/{i}.png'
#     image_path_addicted = f'./teukgang/Drug Addicted or Not People - DANP/test/Addicted/{i}.png'

#     # 중독되지 않은 이미지 예측
#     not_addicted_prob, result = predict_image(image_path_not_addicted)
#     print(f"이미지 '{image_path_not_addicted}'의 중독 확률: {not_addicted_prob} ({result})")

#     # 중독된 이미지 예측
#     addicted_prob, result = predict_image(image_path_addicted)
#     print(f"이미지 '{image_path_addicted}'의 중독 확률: {addicted_prob} ({result})")
