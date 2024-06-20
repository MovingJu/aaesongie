import pandas as pd
import numpy as np

# 엑셀 파일 경로 설정
file_path = "/home/galesky/Downloads/test.xlsx"

# 엑셀 파일 읽기
df = pd.read_excel(file_path)

# 데이터프레임의 열 이름 확인
print(df.columns)

# 필요한 열만 선택
columns_of_interest = ['행정구역별', '시점', '합계출산율', '조출생률(천명당)', '사망건수(명)', '조사망률(천명당)', 
                       '자연증가건수(명)', '자연증가율(천명당)', '혼인건수(건)', '조혼인율(천명당)', 
                       '이혼건수(건)', '조이혼율(천명당)']

# 필터링된 열로 데이터프레임 재구성
df = df[columns_of_interest]

# 연도별로 데이터 처리
years = df['시점'].unique()

# 결과를 저장할 데이터프레임 초기화
result_df = pd.DataFrame(columns=['시점', '행정구역별', '합계출산율과의 상관 계수'])

# 각 연도별로 처리
for year in years:
    # 해당 연도의 데이터 추출
    year_data = df[df['시점'] == year]
    
    # 행정구역별로 상관 계수 계산
    regions = year_data['행정구역별'].unique()
    
    for region in regions:
        # 해당 지역의 데이터 추출
        region_data = year_data[year_data['행정구역별'] == region]
        
        # 합계출산율과 다른 요소들 간의 상관 계수 계산
        corr_with_tfr = region_data.corr()['합계출산율']
        
        # 합계출산율과의 상관 계수만 추출하여 저장
        correlation_value = corr_with_tfr.drop('합계출산율')['합계출산율']
        
        # 결과를 데이터프레임에 추가
        result_df = result_df.append({'시점': year, '행정구역별': region, '합계출산율과의 상관 계수': correlation_value}, ignore_index=True)

# 결과 출력
print("연도별 지역별 합계출산율과의 상관 계수:")
print(result_df)
