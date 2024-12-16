import cv2
import numpy as np
import os

def compare_images(image_path1, image_path2):
    # 이미지 불러오기
    img1 = cv2.imread(image_path1)
    img2 = cv2.imread(image_path2)

    # 이미지가 로드되지 않았을 경우 대비
    if img1 is None or img2 is None:
        return False

    # 이미지 크기와 채널 수가 같은지 확인
    if img1.shape != img2.shape:
        return False

    # 두 이미지를 픽셀 단위로 비교
    difference = cv2.absdiff(img1, img2)
    if np.count_nonzero(difference) == 0:
        return True  # 이미지가 동일함
    else:
        return False  # 이미지가 다름

# 이미지 비교 및 중복 파일 삭제
a = 40  # 테스트 이미지 개수
b = 154  # 학습 이미지 개수

for i in range(1, a + 1):
    for j in range(1, b + 1):
        image_path1 = f'/home/galesky/Documents/GitHub/aaesongie/Lee/python/teukgang/Drug Addicted or Not People - DANP/test/Not Addicted/{i}.png'
        image_path2 = f'/home/galesky/Documents/GitHub/aaesongie/Lee/python/teukgang/Drug Addicted or Not People - DANP/train/Not Addicted/{j}.png'

        try:
            result = compare_images(image_path1, image_path2)
            if result:
                print(f"이미지 같음: {i}, {j}.")
                # os.remove(image_path2)  # 이미지 삭제
        except Exception as e:
            print(f"오류 발생: {e}")
