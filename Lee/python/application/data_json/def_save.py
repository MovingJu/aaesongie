from datetime import datetime

def save_data(self, instance):
    money = self.money_input.text
    note = self.note_input.text

    if money or note:
        # 현재 날짜와 시간 가져오기
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 데이터 저장
        self.store.put(note, amount=money, timestamp=current_time)
        
        # 입력 필드 초기화
        self.money_input.text = ''
        self.note_input.text = ''
        
        print(f"Saved: {money} - {note} at {current_time}")

    else:
        print("Please enter amount and note.")
