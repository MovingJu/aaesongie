from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from collections import defaultdict

import data_json

class TransactionList(Popup):

    def __init__(self, file_path, **kwargs):
        super().__init__(**kwargs)
        self.title = "Transaction List"
        self.size_hint = (0.8, 0.8)
        self.file_path = file_path  # JSON 파일 경로
        self.content = self.show_transaction_list()

    def show_transaction_list(self):
        """트랜잭션 목록을 표시하는 메소드."""
        # 외부 레이아웃 설정
        layout = BoxLayout(orientation='vertical', spacing=10)
        
        # 스크롤 뷰 추가
        scroll_view = ScrollView(size_hint=(1, 1), do_scroll_x=False)
        scroll_layout = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None)
        scroll_layout.bind(minimum_height=scroll_layout.setter('height'))

        # JSON 데이터 읽기
        data = data_json.read_data(self.file_path)

        # 날짜별 그룹화
        grouped_data = defaultdict(list)
        for note, value in data.items():
            timestamp = value.get('timestamp', None)
            if not timestamp:
                continue  # timestamp가 없는 항목은 건너뜀
            date, time = timestamp.split(" ")
            hour, minute = time.split(":")[:2]  # 시간과 분만 추출
            grouped_data[date].append({
                "note": note,  # 사용자가 입력한 note를 저장
                "amount": value.get("amount", "None"),  # amount가 없는 경우 기본값 설정
                "time": f"{hour}:{minute}",
            })

        # 그룹화된 데이터를 레이아웃에 추가
        if grouped_data:
            for date, transactions in grouped_data.items():
                # 날짜 헤더 추가 (큰 글자)
                date_label = Label(
                    text=f"[b]{date}[/b]",
                    size_hint_y=None,
                    height=50,
                    markup=True,
                    font_size='30sp'  # 큰 글자
                )
                scroll_layout.add_widget(date_label)

                # 각 트랜잭션 추가
                for transaction in transactions:
                    transaction_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)

                    # Note (중간 크기 글자)
                    note_label = Label(
                        text=f"{transaction['note']}",
                        size_hint_x=None,
                        width=200,
                        font_size='24sp',  # 중간 글자
                        font_name='NanumGothicBold.ttf'
                    )
                    transaction_box.add_widget(note_label)

                    # Amount와 Time (작은 글자)
                    formatted_amount = f"{int(transaction['amount']):,}"  # 쉼표 추가된 금액
                    details_label = Label(
                        text=f"{formatted_amount} [color=#ff788e]KRW[/color]",  # 금액과 KRW
                        size_hint_x=None,
                        width=200,
                        font_size='19sp',  # 작은 글자
                        markup=True  # 마크업 활성화
                    )
                    transaction_box.add_widget(details_label)

                    # 시간 표시
                    time_label = Label(
                        text=f"{transaction['time']}",
                        size_hint_x=None,
                        width=100,
                        font_size='15sp',  # 작은 글자
                        color=(0.5, 0.5, 1, 1)
                    )
                    transaction_box.add_widget(time_label)

                    # Delete 버튼 추가
                    delete_button = Button(
                        text="Delete",
                        size_hint_x=None,
                        width=100,
                        background_color=(1, 0, 0, 1),  # 빨간색
                        on_press=lambda btn, note=transaction['note']: self.delete_transaction(note)  # note를 참조
                    )
                    transaction_box.add_widget(delete_button)

                    scroll_layout.add_widget(transaction_box)

        else:
            no_data_label = Label(
                text="No transactions found.",
                size_hint_y=None,
                height=30,
                font_size='16sp'
            )
            scroll_layout.add_widget(no_data_label)

        # 스크롤 뷰에 레이아웃 추가
        scroll_view.add_widget(scroll_layout)

        # 외부 레이아웃에 스크롤 뷰 추가
        layout.add_widget(scroll_view)
        return layout

    def delete_transaction(self, note):
        """특정 거래 항목 삭제."""
        data_json.remove_data(self.file_path, note)  # 항목 삭제
        self.refresh_popup()  # 팝업 새로 고침

    def refresh_popup(self):
        """팝업을 새로 고침하여 데이터 갱신."""
        self.content = self.show_transaction_list()
        self.open()  # 팝업 다시 열기
