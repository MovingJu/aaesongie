import numpy as np
from numpy.typing import NDArray

def bogan(n: int, ndot: int, li: list[tuple[float, float]]) -> NDArray[np.float64]: 
    """주어진 점들을 가장 잘 맞추는 다항식의 계수를 반환함.

    Args:
        n (int): 최고차항의 차수
        ndot (int): 점의 개수
        li (list of tuples): 점 순서쌍 리스트 [(x1, y1), (x2, y2), ...]

    Returns:
        NDArray[np.float64]: 다항식 계수를 나타내는 numpy 배열
    """

    if n + 1 > ndot:
        raise ValueError("점의 수가 다항식의 차수보다 많아야 합니다.")

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
            raise ValueError("다항식의 계수를 계산할 수 없습니다. 오류: " + str(e))
    
    else:
        # 과잉 결정된 시스템의 고유공간을 계산
        try:
            # SVD 분해
            U, s, Vt = np.linalg.svd(A)
            
            # 해의 고유공간(기저 벡터) 계산
            tolerance = 1e-10  # 수치적 안정성을 위한 임계값
            rank = np.sum(s > tolerance)
            null_space = Vt.T[:, rank:]
            
            return null_space
        
        except np.linalg.LinAlgError as e:
            raise ValueError("해를 계산할 수 없습니다. 오류: " + str(e))

# 예제 사용
try:
    result = bogan(4, 4, [(1, 3), (2, -2), (3, -5), (4, 0)])
    print("계수 또는 고유공간:", result)
except ValueError as e:
    print("오류:", e)





bogan(1, 2, [(1, 3), (2, 3)])

# if __name__ == 'main':

#     x_arr = []
#     y_arr = []
#     A_arr = []

#     high = input("원하는 함수의 최고차항 차수: ") 
    
#     for i in range(0, int(high)+1, 1):
#         x = float(input("x좌표: "))
#         y_arr.append(float(input("y좌표: ")))
        
#         for j in range(0, int(high)+1, 1):
#             x_arr.append(x**j)

#         A_arr.append(x_arr)

#     print(A_arr)
#     print(y_arr)

# (x1, y1) = (1, 3)
# (x2, y2) = (2, -2)
# (x3, y3) = (3, -5)
# (x4, y4) = (4, 0)

# A = np.array([[1, x1, x1**2, x1**3], [1, x2, x2**2, x2**3], [1, x3, x3**2, x3**3], [1, x4, x4**2, x4**3]])
# iA = np.linalg.inv(A)
# B = [y1, y2, y3, y4]

# print(np.dot(iA, B))


