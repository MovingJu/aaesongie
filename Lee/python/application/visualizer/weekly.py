import matplotlib 
import data_csv.day_seper
matplotlib.rcParams['font.family'] = 'Malgun gothic' # OR NanumMyeongjo
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

import matplotlib.pyplot as plt 
from datetime import datetime
from matplotlib.ticker import ScalarFormatter 


import data_csv
import graph_gen
import graph_text_gen


def preprocessor():
    date, note, amount, total_amount = data_csv.read_data('data_csv/data.csv')

    ymd, hnm, sec = data_csv.time_seper(date)

    year, month, day = data_csv.day_seper(ymd)

    week_day = []


    for i in ymd:

        imsi_date = datetime.strptime(i, "%Y-%m-%d")
        week_day.append(imsi_date.weekday()) # 월요일이 0 - 일요일은 6



    print(len(week_day), len(day))

    indexer = [0]

    for j in range(len(month) - 1):
        if month[j] != month[j + 1]:
            indexer.append(j + 1)

    indexer.append(len(day) + 2)

    month_seper = len(sorted(set(month))) - 1

    xlist = day[indexer[month_seper]:indexer[month_seper+1]]
    ylist = total_amount[indexer[month_seper]:indexer[month_seper+1]]

    return xlist, ylist, month_seper



def weekly_gen():

    xlist, ylist, month_seper = preprocessor()


    fig, ax = graph_gen.graph_gen(xlist, ylist, figsize=(12, 8), 
                                    title=f'{month_seper + 1}월 소비량',
                                    x_rotation=20)

    ax = graph_text_gen.graph_text_gen(xlist, ylist, ax, show_level=1)

    fig.savefig(f'graphs/{month_seper + 1}monthly.png', dpi=200)


if __name__ == "__main__":
    import time

    st = time.time()
    weekly_gen()
    et = time.time()
    print(et - st)
