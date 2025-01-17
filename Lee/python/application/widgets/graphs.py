from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.scatter import Scatter

import data_csv
import visualizer

class Graphs(Popup):

    def __init__(self, file_path, **kwargs):
        super().__init__(**kwargs)
        self.title = "Graphs"
        self.size_hint = (0.8, 0.8)
        self.file_path = file_path
        self.content = self.show_graphs()

    def show_graphs(self):

        date, note, amount, total_amount = data_csv.read_data(self.file_path)

        ymd, hnm, sec = data_csv.time_seper(date)

        year, month, day = data_csv.day_seper(ymd)

        # 외부 레이아웃 설정
        layout = BoxLayout(orientation='vertical', spacing=10)
        
        scroll_view = ScrollView(size_hint=(1, 1), do_scroll_x=False)
        scroll_layout = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None)
        scroll_layout.bind(minimum_height=scroll_layout.setter('height'))

        try:
            # Total graph
            graph_box = BoxLayout(orientation='vertical', size_hint_y=None, height=700)
            img_widget = Image(
                source='visualizer/graphs/total.png',
                allow_stretch=True
            )
            img_widget.bind(on_touch_down=self.show_image_popup)
            graph_box.add_widget(img_widget)
            scroll_layout.add_widget(graph_box)

            monthly_button_box = BoxLayout(orientation='vertical', size_hint_y=None, height=60)  # 높이를 줄임
            monthly_button = Button(
                text="Monthly Graphs",
                font_size=20,  # 폰트 크기 조정
                size_hint=(1, None),  # 버튼의 크기를 박스 크기에 맞춤
                height=50  # 버튼 높이를 줄임
            )
            monthly_button.bind(on_press=self.show_monthly)
            monthly_button_box.add_widget(monthly_button)
            scroll_layout.add_widget(monthly_button_box)




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
    


    def show_monthly(self,instance):
        visualizer.monthly_gen()
        popup = Show_monthly(file_path="data_csv/data.csv")
        popup.open()


    def show_image_popup(self, instance, touch):
        # Check if the touch is on the image widget
        if instance.collide_point(*touch.pos):
            scatter = Scatter(
            scale=6
        )
            image = Image(source=instance.source, allow_stretch=True)
            scatter.add_widget(image)
            
            popup = Popup(
                title="Graph Preview",
                size_hint=(1, 1)
            )
            popup.content = scatter
            popup.open()


class Show_monthly(Popup):
    def __init__(self, file_path, **kwargs):
        super().__init__(**kwargs)
        self.title = "Monthly Graphs"
        self.size_hint = (0.8, 0.8)
        self.file_path = file_path
        self.content = self.show_graphs()

    def show_graphs(self):
         
        date, note, amount, total_amount = data_csv.read_data(self.file_path)

        ymd, hnm, sec = data_csv.time_seper(date)

        year, month, day = data_csv.day_seper(ymd)


        layout = BoxLayout(orientation='vertical', spacing=10)
        
        scroll_view = ScrollView(size_hint=(1, 1), do_scroll_x=False)
        scroll_layout = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None)
        scroll_layout.bind(minimum_height=scroll_layout.setter('height'))

        try:

            for i in range(len(set(month))):
                        graph_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=700)
                        img_widget = Image(
                            source=f'visualizer/graphs/{len(set(month)) - i}monthly.png',
                            allow_stretch=True
                        )
                        img_widget.bind(on_touch_down=self.show_image_popup)
                        graph_box.add_widget(img_widget)
                        scroll_layout.add_widget(graph_box)

        except:
            no_data_label = Label(
                text="Unable to visualize.",
                size_hint_y=None,
                height=30,
                font_size='16sp'
            )
            scroll_layout.add_widget(no_data_label)

        scroll_view.add_widget(scroll_layout)
        layout.add_widget(scroll_view)
        return layout
    


    def show_image_popup(self, instance, touch):
        # Check if the touch is on the image widget
        if instance.collide_point(*touch.pos):
            scatter = Scatter(
            scale=6
        )
            image = Image(source=instance.source, allow_stretch=True)
            scatter.add_widget(image)
            
            popup = Popup(
                title="Graph Preview",
                size_hint=(1, 1)
            )
            popup.content = scatter
            popup.open()