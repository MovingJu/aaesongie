import numpy as np
from numpy.typing import NDArray
import cv2

def bogan(n: int, li: list[tuple[float, float]]) -> NDArray[np.float64]: 
    """주어진 점들을 정확히 지나는 다항함수의 계수를 반환함(선형대수학의 보간법 참고).

    Args:
        n (int): 원하는 함수의 최고차항 차수
        li (list of tuples): 점 순서쌍 리스트 [(x1, y1), (x2, y2), ...]

    Returns:
        NDArray[np.float64]: 다항식 계수를 나타내는 numpy 배열

    Usage Example:
        try:
            result = bogan(3, [(1, 3), (2, -2), (3, -5), (4, 0)])
            print("계수: ", result)
        except ValueError as e:
            print("오류:", e)

    Note: 
        '(최고차항 차수 + 1) == 점의 수' 이어야 작동하며, 그마저도 맞는 함수가 없으면 에러남.
        이상.
    """

    ndot = len(li)

    # 점을 numpy 배열로 변환
    x_vals = np.array([pt[0] for pt in li], dtype=np.float64)
    y_vals = np.array([pt[1] for pt in li], dtype=np.float64)

    # Vandermonde 행렬 생성
    A = np.vander(x_vals, n + 1, increasing=True)

    if n + 1 == ndot:
        # 유일한 해를 계산
        try:
            coeffs = np.linalg.solve(A, y_vals)
            return coeffs
        except np.linalg.LinAlgError as e:
            raise ValueError("다항식의 계수를 계산할 수 없음. 오류: " + str(e))
    
    else:
        raise ValueError("점의 수가 이상함. 함수 설명 참고.")

def lsm(n: int, li: list[tuple[float, float]]) -> NDArray[np.float64]: 
    """주어진 점들과 오차가 가장 적은 다항함수를 반환함(선형대수학 최소제곱법 참고).

    Args:
        n (int): 원하는 함수의 최고차항 차수
        li (list of tuples): 점 순서쌍 리스트 [(x1, y1), (x2, y2), ...]

    Returns:
        NDArray[np.float64]: 다항식 계수를 나타내는 numpy 배열

    Usage Example:
        try:
            result = lsm(1, [(0, 1), (1, 3), (2, 4), (3, 4)])
            print("계수:", result)

        except ValueError as e:
            print("오류:", e)

    Note: 
        일차함수를 넣는게 정석. 점의 위치를 보면서 최고차항의 계수를 적당히 입력하는걸 추천함.
        이상.
    """

    ndot = len(li)

    # 점을 numpy 배열로 변환
    x_vals = np.array([pt[0] for pt in li], dtype=np.float64)
    y_vals = np.array([pt[1] for pt in li], dtype=np.float64)

    # Vandermonde 행렬 생성
    A = np.vander(x_vals, n + 1, increasing=True)
    A1 = np.dot(A.T, A)
    y_vals = np.dot(A.T, y_vals)

    try:
        coeffs = np.linalg.solve(A1, y_vals)
        return coeffs
    
    except np.linalg.LinAlgError as e:
        raise ValueError("다항식의 계수를 계산할 수 없음. 오류: " + str(e))
    

def img_com(image: NDArray) -> tuple[NDArray, NDArray, NDArray, bool]:
    """이미지를 RAM 덜 차지하는 행렬, 벡터, 행렬, bool(흑백 여부)로 반환하는 함수(선형대수학 이미지 압축 원리 참고)
    Args:
        image (NDArray): cv2로 읽어온 이미지
    
    Return: 
        tuple(행렬, 벡터, 행렬, 참/거짓(흑백 여부))

    Usage example:
        tu = img_com(dodo)

    Note:
        화질이 조금 나빠지나, 변수들을 다룰때 공간을 덜 차지함(저장된 사진의 크기는 동일함).
        이상.
    """
    if len(image.shape) == 2:
        U, S, VT = np.linalg.svd(image, full_matrices=False)

        S = S[:int(len(S)/6)]
        U = U[:, :len(S)]
        VT = VT[:len(S), :]

        return U, S, VT, True
    
    else:
        blu, gre, red = cv2.split(image)
        image1 = [blu, gre, red]

        U_list, S_list, VT_list = [], [], []

        for channel in image1:
            U, S, VT = np.linalg.svd(channel, full_matrices=False)

            S = S[:int(len(S)/6)]
            U = U[:, :len(S)]
            VT = VT[:len(S), :]

            U_list.append(U)
            S_list.append(S)
            VT_list.append(VT)

        return np.array(U_list), np.array(S_list), np.array(VT_list), False
    
def img_cons(li: tuple[NDArray, NDArray, NDArray, bool]) -> NDArray:
    """img_com으로 변형한 이미지를 원리대로 되돌려놓는 함수.

    Args:
        li (tuple): img_com 함수로부터 나온 튜플
            - U (NDArray): U 행렬들
            - S (NDArray): S 벡터들
            - VT (NDArray): VT 행렬들
            - bool: 이미지의 흑백 여부

    Returns:
        NDArray: 복원된 이미지 행렬, cv2로 이미지화 가능

    Usage example:
        cv2.imwrite('image.jpg', img_cons(li))
    """
    U_list, S_list, VT_list, is_grayscale = li

    if is_grayscale:
        S_diag = np.diag(S_list)
        restored_image = np.dot(U_list, np.dot(S_diag, VT_list))
    else:
        restored_channels = []
        for U, S, VT in zip(U_list, S_list, VT_list):
            S_diag = np.diag(S)

            # 복원된 채널 계산
            restored_channel = np.dot(U, np.dot(S_diag, VT))

            # 추가: 데이터 유형 및 범위 설정
            restored_channel = np.clip(restored_channel, 0, 255)
            restored_channels.append(restored_channel.astype(np.uint8))

        restored_image = cv2.merge(restored_channels)

    return restored_image


if __name__ == "__main__":

    print("bogan(3, [(1, 3), (2, -2), (3, -5), (4, 0)])")
    try:
        result = bogan(3, [(1, 3), (2, -2), (3, -5), (4, 0)])
        print("계수:", result)
    except ValueError as e:
        print("오류:", e)

    print("lsm(1, [(0, 1), (1, 3), (2, 4), (3, 4)])")
    try:
        result = lsm(1, [(0, 1), (1, 3), (2, 4), (3, 4)])
        print("계수:", result)

    except ValueError as e:
        print("오류:", e)