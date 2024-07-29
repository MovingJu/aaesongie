import numpy as np
import cv2

# 임의의 흑백 이미지 행렬 생성
gray_image_array = np.array([
    [0, 128, 255, 64],
    [192, 255, 0, 128],
    [64, 0, 192, 255]
], dtype=np.uint8)

# 이미지 행렬 출력 (디버깅 용도)
print('임의의 흑백 이미지 행렬:')
print(gray_image_array)

# 이미지 윈도우에 표시
cv2.imshow('Gray Image', gray_image_array)
cv2.waitKey(0)  # 아무 키나 누르면 윈도우 닫기
cv2.destroyAllWindows()
