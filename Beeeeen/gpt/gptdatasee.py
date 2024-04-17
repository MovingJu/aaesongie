import matplotlib.pyplot as plt

# 데이터 생성
x = []
y = []

for i in range(-100,101):
    x.append(i)
    y.append(i**2 + 2*i + 1)

# 선 그래프
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('')
plt.show()
