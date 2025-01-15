import pandas as pd


def remove_data(file_path:str, date:str) -> None:
    """특정 거래 항목 삭제."""
    
    print(file_path, date)
    
    try:
        df = pd.read_csv(file_path)

        # print(df)

        df = df[~(df['date'].astype(str) == str(date))] # not 연산자 주의할 것.

        df.to_csv(file_path, index=False)

        # print(df)
        
        
    except Exception as e:
        print(f"Error while deleting transaction: {e}")


if __name__ == "__main__":
    remove_data('data_csv/data.csv', '2025-01-12/17:13;05')