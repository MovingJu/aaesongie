import numpy as np
import matplotlib.pyplot as plt

# 유리함수 정의
def rational_function(x):
    return 1 / (x**2 - 1)

# x 값 생성
x = np.linspace(-2, 2, 400)

# 함수값 계산
y = rational_function(x)

# 그래프 그리기
plt.plot(x, y)
plt.title('Rational Function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
