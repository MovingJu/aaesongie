import pandas as pd

boo = {'이름':['ㅎㅎㅂ','ㅇㄷㅈ','ㄱㅅㅇ','ㄴㅈㅎ'],
       '나이':[11,12,13,14],
       '직군':['ㅃ','ㅉ','ㄸ','ㄲ']}

df = pd.DataFrame(boo)
print(df)

newboo = {'이름':['ㅇㅈㅅ'],
          '나이':[15],
          '직군':['ㅆ']}

newdf = pd.DataFrame(newboo, index=[1])
df = pd.concat([df, newdf], ignore_index=True)
print(df)

print(df[df['나이'] >= 13])

df.loc[df['이름'] == 'ㅇㄷㅈ', '나이'] = 30

print(df)

# import pandas as pd
# import matplotlib.pyplot as plt

# # 데이터프레임 생성
# data = {'날짜': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'],
#         '판매량': [100, 120, 90, 110]}
# df = pd.DataFrame(data)

# # 날짜를 인덱스로 설정
# df['날짜'] = pd.to_datetime(df['날짜'])
# df.set_index('날짜', inplace=True)

# # 시각화
# df.plot(kind='line', marker='o')
# plt.title('일별 판매량 추이')
# plt.xlabel('날짜')
# plt.ylabel('판매량')
# plt.grid(True)
# plt.show()

# import pandas as pd

# 리스트를 사용하여 시리즈 생성
# data = [1, 2, 3, 4, 5]
# s = pd.Series(data)

# print(s)
