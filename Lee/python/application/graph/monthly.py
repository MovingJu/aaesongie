import matplotlib
import data_csv.day_seper
matplotlib.rcParams['font.family'] = 'NanumMyeongjo'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

import matplotlib.pyplot as plt
import data_csv
import time
from matplotlib.ticker import ScalarFormatter



### to do: 날짜별로 slicing해줘서 관리하기 용이하게 하는 함수 제작 필요. -> 비슷한건 이 파일 아래에 구현돼있음.




def monthly_gen():

    date, note, amount, total_amount = data_csv.read_data('data_csv/data.csv')

    ymd, hnm, sec = data_csv.time_seper(date)

    year, month, day = data_csv.day_seper(ymd)

    month_seted = sorted(set(month))


    for i in month_seted:
        pass

    indexer = [0]

    for j in range(len(month) - 1):
        if month[j] != month[j + 1]:
            indexer.append(j + 1)

    indexer.append(len(day) + 2)

    print(indexer)


    for k in range(len(sorted(set(month)))):

        # 그래프 크기 설정
        plt.figure(figsize=(12, 8), facecolor='gray')  # 그래프 크기 조정
        
        plt.plot(day[indexer[k]:indexer[k+1]], total_amount[indexer[k]:indexer[k+1]], color='black', 
                 marker='o', linestyle='-.')


        for idx, txt in enumerate(total_amount[indexer[k]:indexer[k+1]]):
            txt = round(total_amount[indexer[k]:indexer[k+1]][idx]/1e6, 3)

            plt.text(day[indexer[k]:indexer[k+1]][idx], total_amount[indexer[k]:indexer[k+1]][idx] + 0.4, txt, 
                     ha='center', color='blue', rotation=20)



        plt.title(f'{k+1}월 소비량')

        ax = plt.gca()
        ax.set_facecolor('gray') 


        plt.xlabel('날짜', loc='left', color='black')
        plt.ylabel('총액', loc='center', color='black')

        plt.xticks(rotation=20, ha='center')

        #x축 간격을 이틀로 설정
        plt.xticks(range(0, len(day[indexer[k]:indexer[k+1]]), 2), day[indexer[k]:indexer[k+1]][::2])

        plt.grid(color='black', alpha=0.5, linestyle='--', linewidth=1)

        plt.savefig(f'{k + 1}monthly.png', dpi=150)


if __name__ == "__main__":
    st = time.time()
    monthly_gen()
    et = time.time()
    print(et - st)
