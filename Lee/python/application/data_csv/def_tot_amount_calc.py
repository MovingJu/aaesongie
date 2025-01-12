import pandas as pd
import data_csv


def tot_amount_calc(input_amount):

    date, note, amount, tot_amount_li = data_csv.read_data('data_csv/data.csv')
    df = pd.read_csv('data_csv/data.csv')


    for i in range(len(tot_amount_li) - 1):
        df.loc[i + 1, 'total_amount'] = df.loc[i, 'total_amount'] + df.loc[i + 1, 'amount']

    # df.to_csv('data_csv/data.csv', index=False)
    print(df)


    total_amount = tot_amount_li[len(tot_amount_li) - 1] + float(input_amount)

    return total_amount, df



##### to do: df에 total_amount 전체 적용값 변경은 되는데 저장은 안되는 기이한 현상 발생중.