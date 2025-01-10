from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

import data_csv




class TransactionList(Popup):

    def __init__(self, file_path, **kwargs):
        super().__init__(**kwargs)
        self.title = "Transaction List"
        self.size_hint = (0.8, 0.8)
        self.file_path = file_path  # CSV 파일 경로
        self.content = self.show_transaction_list()

    def show_transaction_list(self):
        """트랜잭션 목록을 날짜별로 필터링하여 표시하는 메소드."""
        # 외부 레이아웃 설정
        layout = BoxLayout(orientation='vertical', spacing=10)
        
        # 스크롤 뷰 추가
        scroll_view = ScrollView(size_hint=(1, 1), do_scroll_x=False)
        scroll_layout = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None)
        scroll_layout.bind(minimum_height=scroll_layout.setter('height'))

        # JSON 데이터 읽기
        try: 
            date, note, amount = data_csv.read_data(self.file_path)

            print(date)

            # 날짜별로 데이터를 분리
            (day, hnm, sec) = data_csv.time_seper(date)

            print(day, hnm, sec)

            date_set = sorted(set(day))  # 날짜 목록을 정렬
            
            for one_day in date_set:

                # 날짜 헤더 추가 (큰 글자)
                date_label = Label(
                    text=f"[b]{one_day}[/b]",
                    size_hint_y=None,
                    height=50,
                    markup=True,
                    font_size='15sp'  # 큰 글자
                )
                scroll_layout.add_widget(date_label)


                for i in range(len(date)):

                    transaction_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
                    

                    print(date)

                    print(note[i], type(note[i]))

                    # Note (중간 크기 글자)
                    note_label = Label(
                        text=f"{str(note[i])}",
                        size_hint_x=None,
                        width=200,
                        font_size='12sp',  # 중간 글자
                        font_name='NanumGothicBold.ttf'
                    )
                    transaction_box.add_widget(note_label)

                    # Amount
                    print(amount[i], type(amount[i]))

                    formatted_amount = f"{int(amount[i]):,}"  # 쉼표 추가된 금액
                    details_label = Label(
                        text=f"{formatted_amount} [color=#ff788e]KRW[/color]",  # 금액과 KRW
                        size_hint_x=None,
                        width=200,
                        font_size='10sp',  # 작은 글자
                        markup=True  # 마크업 활성화
                    )
                    transaction_box.add_widget(details_label)

                    # 시간 표시
                    print(hnm[i], type(hnm[i]))

                    time_label = Label(
                        text=f"{str(hnm[i])}",
                        size_hint_x=None,
                        width=100,
                        font_size='7sp',  # 작은 글자
                        color=(0.5, 0.5, 1, 1)
                    )
                    transaction_box.add_widget(time_label)

                    # Delete 버튼 추가
                    delete_button = Button(
                        text="Delete",
                        size_hint_x=None,
                        font_size='8sp',
                        width=100,
                        background_color=(1, 0, 0, 1),  # 빨간색
                        on_press=lambda btn, day=date: self.delete_transaction(day)
                    )
                    transaction_box.add_widget(delete_button)

                    scroll_layout.add_widget(transaction_box)

        except Exception as e:
            no_data_label = Label(
                text="No transactions found or Unable to open it.",
                size_hint_y=None,
                height=30,
                font_size='16sp'
            )

            print("error code: " + str(e))

            scroll_layout.add_widget(no_data_label)

        
        # 스크롤 뷰에 레이아웃 추가
        scroll_view.add_widget(scroll_layout)

        # 외부 레이아웃에 스크롤 뷰 추가
        layout.add_widget(scroll_view)
        return layout

    def delete_transaction(self, date):
        """특정 거래 항목 삭제."""
        data_csv.remove_data(self.file_path, date)  # 항목 삭제
        self.refresh_popup()  # 팝업 새로 고침

    def refresh_popup(self):
        """팝업을 새로 고침하여 데이터 갱신."""
        self.content = self.show_transaction_list()
        self.open()  # 팝업 다시 열기
