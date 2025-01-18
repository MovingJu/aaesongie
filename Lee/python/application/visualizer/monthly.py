import data_csv
import visualizer


def preprocessor():
    # date, note, amount, total_amount = data_csv.read_data('data_csv/data.csv')

    ymd, amount, total_amount = data_csv.read_set_data('data_csv/data.csv')


    year, month, day = data_csv.day_seper(ymd)


    month_seted = sorted(set(month))


    indexer = [0]

    for j in range(len(month) - 1):
        if month[j] != month[j + 1]:
            indexer.append(j + 1)

    indexer.append(len(day) + 2)

    return month, indexer, day, total_amount



def monthly_gen():

    month, indexer, day, total_amount = preprocessor()


    for k in range(len(sorted(set(month)))):

        xlist = day[indexer[k]:indexer[k+1]]
        ylist = total_amount[indexer[k]:indexer[k+1]]

        fig, ax = visualizer.graph_gen(xlist, ylist, figsize=(12, 8), 
                                      title=f'{k + 1}M\'s Spent Amount',
                                      x_rotation=20)

        ax = visualizer.graph_text_gen(xlist, ylist, ax, show_level=1)

        fig.savefig(f'visualizer/graphs/{k + 1}monthly.png', dpi=200)


if __name__ == "__main__":
    import time

    st = time.time()
    monthly_gen()
    et = time.time()
    print(et - st)
