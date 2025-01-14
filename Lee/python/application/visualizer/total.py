import matplotlib 
import data_csv.day_seper
matplotlib.rcParams['font.family'] = 'Malgun gothic' # OR NanumMyeongjo
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

import matplotlib.pyplot as plt 
from matplotlib.ticker import ScalarFormatter 

import data_csv
import graph_gen
import graph_text_gen


def preprocess_total_data():
    date, note, amount, total_amount = data_csv.read_data('data_csv/data.csv')
    ymd, hnm, sec = data_csv.time_seper(date)
    year, month, day = data_csv.day_seper(ymd)

    # 날짜와 월/일 조합 리스트 생성
    mnd = [f"{month[i]}-{day[i]}" for i in range(len(month))]

    return mnd, total_amount



def total_gen():

    mnd, total_amount = preprocess_total_data()

    xticks = int(len(mnd)/20)

    fig, ax = graph_gen.graph_gen(mnd, total_amount, xticks=xticks, title='총액')

    ax = graph_text_gen.graph_text_gen(mnd, total_amount, ax, show_level=2)


    fig.savefig(f'graphs/total.png', dpi=200)


if __name__ == "__main__":
    import time

    st = time.time()
    total_gen()
    et = time.time()
    print(et - st)
