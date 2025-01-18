import data_csv
import visualizer


def preprocess_total_data():
    ymd, amount, total_amount = data_csv.read_set_data('data_csv/data.csv')

    year, month, day = data_csv.day_seper(ymd)

    print(month, day)

    # 날짜와 월/일 조합 리스트 생성
    mnd = [f"{month[i]}-{day[i]}" for i in range(len(month))]

    return mnd, total_amount



def total_gen():

    mnd, total_amount = preprocess_total_data()

    xticks = max(int(len(mnd)/20), 1)

    fig, ax = visualizer.graph_gen(mnd, total_amount, xticks=xticks, title='Total')

    ax = visualizer.graph_text_gen(mnd, total_amount, ax, show_level=2)


    fig.savefig(f'visualizer/graphs/total.png', dpi=200)


if __name__ == "__main__":
    import time

    st = time.time()
    total_gen()
    et = time.time()
    print(et - st)
