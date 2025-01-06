import json

def remove_data(file_path, note):
    """특정 거래 항목 삭제."""
    try:
        # JSON 파일 읽기
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # 해당 항목 삭제
        if note in data:
            del data[note]
            # JSON 파일에 다시 저장
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
        print('removed!')
        
    except Exception as e:
        print(f"Error while deleting transaction: {e}")
