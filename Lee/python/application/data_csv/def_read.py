import pandas as pd

from datetime import datetime, timedelta

import data_csv

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

    # Read data from CSV
    date, note, amount, total_amount = read_data(file_path)

    # Separate date into year, month, day
    ymd, _, _ = data_csv.time_seper(date)

    # Prepare lists to accumulate final data
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

    # Detect and fill missing dates
    final_ymd = []
    final_amount = []
    final_total = []

    current_total = total_amount1[0] if total_amount1 else 0
    current_date = datetime.strptime(ymd1[0], "%Y-%m-%d")  # Start date
    end_date = datetime.strptime(ymd1[-1], "%Y-%m-%d")  # End date

    ymd_index = 0  # Index to track input data dates

    while current_date <= end_date:
        formatted_date = current_date.strftime("%Y-%m-%d")

        if ymd_index < len(ymd1) and formatted_date == ymd1[ymd_index]:
            # If date exists in original data
            final_ymd.append(formatted_date)
            final_amount.append(amount1[ymd_index])
            current_total = total_amount1[ymd_index]
            final_total.append(current_total)
            ymd_index += 1
        else:
            # Fill missing date
            final_ymd.append(formatted_date)
            final_amount.append(0)
            final_total.append(current_total)

        current_date += timedelta(days=1)

    return final_ymd, final_amount, final_total

    

if __name__ == "__main__":
    print(read_set_data("data_csv/data.csv"))