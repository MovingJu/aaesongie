import numpy as np
from numpy.typing import NDArray

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