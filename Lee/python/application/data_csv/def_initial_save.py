import pandas as pd
import datetime


def save_initial_data(self, instance):

    df = pd.read_csv(self.file_path)

    dt = datetime.datetime.today().strftime("%Y-%m-%d/%H:%M;%S")

    new_row = pd.DataFrame([{'date': dt, 'note': self.note_input.text, 
    'amount': self.money_input.text, 'total_amount':self.total_amount.text}])


    df = pd.concat([df, new_row], ignore_index=True)


    print(df)

    df.to_csv(self.file_path, index=False)