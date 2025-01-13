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

if __name__ == "__main__":
    print(read_data("data_csv/data.csv"))