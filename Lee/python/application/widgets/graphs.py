from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from collections import defaultdict

import data_csv


### to do: graph버튼을 누르고 들어오면, total_graph만 보이고 monthly, weekly 버튼이 2개 있게 하기, 
### monthly 버튼을 누르면 아래의 코드처럼 달마다의 그래프 보여주기(역순으로)

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

            graph_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=500)
            img_widget = Image(
                source='visualizer/graphs/total.png'
            )
            graph_box.add_widget(img_widget)
            scroll_layout.add_widget(graph_box)



            # graph_box.add_widget(Button(text="Monthly", font_size=32, height=80,
            #                       on_press=self.show_monthly))
            # scroll_layout.add_widget(graph_box)


            for i in range(len(set(month))):
                graph_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=450)

                img_widget = Image(
                source=f'visualizer/graphs/{len(set(month)) - i}monthly.png'
                )

                graph_box.add_widget(img_widget)
                scroll_layout.add_widget(graph_box)


        except Exception as e:
            no_data_label = Label(
                text="Unable to visualize.",
                size_hint_y=None,
                height=30,
                font_size='16sp'
            )

            print("error code: " + str(e))

            scroll_layout.add_widget(no_data_label)


        scroll_view.add_widget(scroll_layout)
        layout.add_widget(scroll_view)
        return layout

    def show_monthly(self):
        return
