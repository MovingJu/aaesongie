import matplotlib.pyplot as plt

# 복숭아의 형태를 나타내는 데이터 생성
x = [0, 1, 2, 3, 4, 5, 6, 7]
y = [2, 3, 3.5, 3.5, 3, 2.5, 2, 0]

# 복숭아 그리기
plt.plot(x, y, color='orange', linewidth=2)

# 그래프에 타이틀 추가
plt.title('Peach')

# x, y 축에 라벨 추가
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 그래프 표시
plt.show()
