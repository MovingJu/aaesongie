import pandas as pd
import data_csv


def tot_amount_calc():

    """data.csv의 total_amount값 정확히 계산해서 저장하는 함수."""

    _, _, _, tot_amount_li = data_csv.read_data('data_csv/data.csv')
    df = pd.read_csv('data_csv/data.csv')


    for i in range(len(tot_amount_li) - 1):
        df.loc[i + 1, 'total_amount'] = df.loc[i, 'total_amount'] + df.loc[i + 1, 'amount']

    df.to_csv('data_csv/data.csv', index=False)



def tot_amount_reter(input_amount):
    
    """def_save.py용 함수."""

    _, _, _, tot_amount_li = data_csv.read_data('data_csv/data.csv')

    total_amount = tot_amount_li[len(tot_amount_li) - 1] + float(input_amount)

    return total_amount
