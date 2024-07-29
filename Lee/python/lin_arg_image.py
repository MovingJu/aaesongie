import numpy as np
import cv2

# 이미지 파일을 불러옵니다
image_path = 'doggy.png'

# 흑백 이미지로 불러오기
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

U, S, VT = np.linalg.svd(gray_image)

S = S[:50]
VT1 = VT[:len(S), :len(VT[0])]
U1 = U[:len(U), :len(S)]
S1 = np.diag(S)

print(U1.shape, S.shape, VT1.shape)

# # 이미지 윈도우에 표시
# cv2.imshow('Gray Image', np.dot(U, np.dot(S1, VT1)))
# cv2.waitKey(0)  # 아무 키나 누르면 윈도우 닫기
# cv2.destroyAllWindows()


print(f'{gray_image.nbytes}, {U1.nbytes + S.nbytes + VT1.nbytes}')
print(f'{(U1.nbytes + S.nbytes + VT1.nbytes)/gray_image.nbytes: .2f} times bigger')

output_path = 'gray_image.png'
cv2.imwrite(output_path, gray_image.astype(np.uint8))
print(f'복원된 이미지를 {output_path}로 저장했습니다.')