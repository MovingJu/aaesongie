from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from collections import defaultdict

import data_csv

class Graphs(Popup):

    def __init__(self, file_path, **kwargs):
        super().__init__(**kwargs)
        self.title = "Graphs"
        self.size_hint = (0.8, 0.8)
        self.file_path = file_path  # JSON 파일 경로
        self.content = self.show_graphs()


        

    def show_graphs(self):
        """트랜잭션 목록을 표시하는 메소드."""

        date, note, amount, total_amount = data_csv.read_data('data_csv/data.csv')

        ymd, hnm, sec = data_csv.time_seper(date)

        year, month, day = data_csv.day_seper(ymd)



        # 외부 레이아웃 설정
        layout = BoxLayout(orientation='vertical', spacing=10)
        

        scroll_view = ScrollView(size_hint=(1, 1), do_scroll_x=False)
        scroll_layout = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None)
        scroll_layout.bind(minimum_height=scroll_layout.setter('height'))

        try:


            for i in range(len(set(month))):
                graph_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=450)

                img_widget = Image(
                source=f'visualizer/graphs/{i + 1}monthly.png',  # 이미지 파일 경로
                # size_hint_x=None,
                # width=0,  # 이미지 가로 크기
                # keep_ratio=True,
                # allow_stretch=True
                )

                graph_box.add_widget(img_widget)

                scroll_layout.add_widget(graph_box)


        except Exception as e:
            no_data_label = Label(
                text="No graphs found or Unable to open it.",
                size_hint_y=None,
                height=30,
                font_size='16sp'
            )

            print("error code: " + str(e))

            scroll_layout.add_widget(no_data_label)


        scroll_view.add_widget(scroll_layout)
        layout.add_widget(scroll_view)
        return layout

    def delete_transaction(self, note):
        """특정 거래 항목 삭제."""
        data_csv.remove_data(self.file_path, note)  # 항목 삭제
        self.refresh_popup()  # 팝업 새로 고침

    def refresh_popup(self):
        """팝업을 새로 고침하여 데이터 갱신."""
        self.content = self.show_transaction_list()
        self.open()  # 팝업 다시 열기
