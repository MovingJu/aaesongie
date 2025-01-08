import pandas as pd
import datetime


def save_data(self, instance):

    df = pd.read_csv(self.file_path)

    dt = datetime.datetime.today().strftime("%Y;%m;%d/%H;%M;%T")

    new_row = pd.DataFrame([{'date': dt, 'note': self.note_input.text, 'amount': self.money_input.text}])


    df = pd.concat([df, new_row], ignore_index=True)


    print(df)

    df.to_csv(self.file_path, index=False)