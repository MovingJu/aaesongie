import pandas as pd
import data_csv

def tot_amount_calc() -> 'pd.DataFrame':
    """total_amount 계산시켜서 저장하는 코드"""
    _, _, amount, tot_amount_calc = data_csv.read_data('data_csv/data.csv')

    df = pd.read_csv('data_csv/data.csv')

    for i in range(len(amount)):
        if amount[i] != None:

            if tot_amount_calc[i] == None:
                tot_amount_calc[i] = 0

            tot_amount_calc[i] = tot_amount_calc[i - 1] + amount[i]

        else:
            continue

    df['total_amount'] = tot_amount_calc
    df.to_csv('data_csv/data.csv', index=False)

    return df


if __name__ == "__main__":
    print(tot_amount_calc())