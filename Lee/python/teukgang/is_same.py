import cv2
import numpy as np

def compare_images(image_path1, image_path2):
    # 이미지 불러오기
    img1 = cv2.imread(image_path1)
    img2 = cv2.imread(image_path2)

    # 이미지 크기와 채널 수가 같은지 확인
    if img1.shape != img2.shape:
        return False

    # 두 이미지를 픽셀 단위로 비교
    difference = cv2.absdiff(img1, img2)
    if np.count_nonzero(difference) == 0:
        return True  # 이미지가 동일함
    else:
        return False  # 이미지가 다름

# 예시 사용법

a = 40
b = 160


for i in range(1, a + 1, 1):
    for j in range(1, b + 1, 1):
        
        image_path1 = f'./Drug Addicted or Not People - DANP/test/Not Addicted/{i}.png'
        image_path2 = f'./Drug Addicted or Not People - DANP/train/Not Addicted/{j}.png'

        result = compare_images(image_path1, image_path2)
        if result:
            print(f"이미지 같음: {i}, {j}")