import pandas as pd


def save_initial_data(file_path, total_amount):

    total_amount = int(total_amount.text)

    df = pd.DataFrame({
        'date':[None],
        'note':[None],
        'amount':[None],
        'total_amount':[total_amount]
    })


    print(df)

    df.to_csv(file_path, index=False)