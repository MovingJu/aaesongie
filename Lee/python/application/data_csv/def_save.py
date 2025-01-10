import pandas as pd
import datetime
import data_csv


def save_data(file_path, note_input, money_input, total_amount):

    df = pd.read_csv(file_path)

    dt = datetime.datetime.today().strftime("%Y-%m-%d/%H:%M;%S")

    new_row = pd.DataFrame([{'date': dt, 'note': note_input.text, 
    'amount': money_input.text, 'total_amount':total_amount}])


    df = pd.concat([df, new_row], ignore_index=True)



    df.to_csv(file_path, index=False)

    data_csv.tot_amount_calc()

    # print(df)