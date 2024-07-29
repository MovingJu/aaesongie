import numpy as np
import cv2

# 이미지 파일을 불러옵니다
dodo = cv2.imread('dodo.jpg')
print(dodo.shape)

# 채널 분리
blu, gre, red = cv2.split(dodo)

# 각 채널을 저장할 리스트
dodo1 = [blu, gre, red]

# 총 바이트 수 계산용 변수
tot_bytes = 0

# 각 채널에 대해 SVD 수행 및 복원
for rep in range(3):
    
    # SVD 수행
    U, S, VT = np.linalg.svd(dodo1[rep], full_matrices=False)
    
    # SVD를 통한 채널 복원
    k = min(100, len(S))
    S = S[:k]
    S = np.array(S, dtype=np.int32)
    S1 = np.diag(S)
    VT1 = VT[:len(S), :]
    U1 = U[:, :len(S)]

    print(S)
    print(S.nbytes)
    
    # 채널 복원
    dodo1[rep] = np.dot(U1, np.dot(S1, VT1))
    
    # 총 바이트 수 계산
    tot_bytes += (S.nbytes + VT1.nbytes + U1.nbytes)

# 채널을 합쳐 색상 이미지 복원
image = cv2.merge((dodo1[0], dodo1[1], dodo1[2]))

# 색상 이미지 복원된 이미지 타입을 uint8로 변환 (픽셀 값이 0-255 범위에 있도록 클리핑)
image = np.clip(image, 0, 255).astype(np.uint8)

# 결과 출력
print(f'Original image size (bytes): {dodo.nbytes}')
print(f'Total size after SVD operations (bytes): {tot_bytes}')
print(f'Ratio of total size to original size: {tot_bytes / dodo.nbytes:.2f}')

# 복원된 이미지 저장
cv2.imwrite('image.jpg', image)
print('복원된 이미지가 저장되었습니다: image.jpg')