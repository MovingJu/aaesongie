import pandas as pd


def save_initial_data(file_path, total_amount):

    total_amount = int(total_amount.text)

    df = pd.DataFrame({
        'date':['2025-01-01/00:00;00'],
        'note':['Initial A'],
        'amount':[None],
        'total_amount':[total_amount]
    })


    print(df)

    df.to_csv(file_path, index=False)