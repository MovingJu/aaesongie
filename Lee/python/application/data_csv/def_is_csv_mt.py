import pandas as pd

def is_csv_mt(file_path):
    try:
        df = pd.read_csv(file_path)
        return False
    except FileNotFoundError:
        return True 
    except pd.errors.EmptyDataError:
        return True

if __name__ == "__main__":
    file_path = 'data_csv/data.csv'
    print(is_csv_mt(file_path))
