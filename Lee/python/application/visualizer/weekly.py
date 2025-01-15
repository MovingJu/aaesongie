import matplotlib.pyplot as plt 
from datetime import datetime
from matplotlib.ticker import ScalarFormatter 


import data_csv
import visualizer


def preprocessor():
    ymd, amount, total_amount = data_csv.read_set_data('data_csv/data.csv')

    year, month, day = data_csv.day_seper(ymd)


    week_day = []


    for i in ymd:

        imsi_date = datetime.strptime(i, "%Y-%m-%d")
        week_day.append(imsi_date.weekday()) # 월요일이 0 - 일요일은 6



    print(week_day, len(day))

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


    fig, ax = visualizer.graph_gen(xlist, ylist, figsize=(12, 8), 
                                    title=f'{month_seper + 1}월 소비량',
                                    x_rotation=20)

    ax = visualizer.graph_text_gen(xlist, ylist, ax, show_level=1)

    fig.savefig(f'visualizer/graphs/{month_seper + 1}monthly.png', dpi=200)


if __name__ == "__main__":
    import time

    st = time.time()
    weekly_gen()
    et = time.time()
    print(et - st)
