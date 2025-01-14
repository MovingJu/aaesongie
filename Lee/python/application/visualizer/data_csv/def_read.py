import pandas as pd

def read_data(file_path: str) -> tuple[list[str], list[str], list[int], list[float]]:
    """csv파일의 열들을 리스트로 반환함."""
    
    df = pd.read_csv(file_path)

    date, note, amount, total_amount = [], [], [], []

    for i in range(len(df)):


        if i in df.index and (not pd.isna(df['date'][i])):
            date.append(str(df['date'][i]))
        else:
            date.append(None)


        if i in df.index and (not pd.isna(df['note'][i])):
            note.append(str(df['note'][i]))
        else:
            note.append(None)


        if i in df.index and (not pd.isna(df['amount'][i])):
            amount.append(int(df['amount'][i]))
        else:
            amount.append(None)

        if i in df.index and (not pd.isna(df['total_amount'][i])):
            total_amount.append(int(df['total_amount'][i]))
        else:
            total_amount.append(None)


    return date, note, amount, total_amount


def read_set_data(file_path):
    import data_csv

    date, note, amount ,total_amount = read_data(file_path)

    ymd, _, _ = data_csv.time_seper(date)

    ymd1 = []
    amount1 = []
    total_amount1 = []
    

    for i in range(len(ymd)):
        if ymd[i - 1] == ymd[i]:
                total_amount1[-1] = total_amount[i]

                amount1[-1] += amount[i]

        else:
            ymd1.append(ymd[i])
            amount1.append(amount[i])
            total_amount1.append(total_amount[i])

    return ymd1, amount1, total_amount1
    

if __name__ == "__main__":
    print(read_data("data_csv/data.csv"))