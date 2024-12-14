import numpy as np
import cv2
from lin_arg import *

# 이미지 읽기
dodo = cv2.imread('Lee/python/dodo.jpg')

# img_com 함수는 이미지 dodo를 a, b, c, d로 분리한다고 가정합니다.
# img_com은 정의되어 있어야 하며, 이 함수가 반환하는 것이 올바른 이미지 데이터인지 확인해야 합니다.
a, b, c, d = img_com(dodo)

# img_cons 함수가 이미지 리스트를 하나의 이미지로 결합한다고 가정합니다.
# img_cons도 정의되어 있어야 하며, 결합된 이미지가 올바른 포맷인지 확인해야 합니다.
combined_image = img_cons([a, b, c, d])

# 파일 저장 (파일 경로에 확장자 추가)
success = cv2.imwrite('Lee/python/dodo1.jpg', combined_image)

# 저장 성공 여부 확인
if success:
    print("이미지가 성공적으로 저장되었습니다.")
else:
    print("이미지를 저장하는 데 실패했습니다.")
