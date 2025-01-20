from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Rotate

import data_csv
import visualizer

class Graphs(Popup):
    def __init__(self, file_path, **kwargs):
        super().__init__(**kwargs)
        self.title = "Graphs"
        self.size_hint = (1, 1)
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
            # Add Total Graph
            self.add_graph(scroll_layout, 'visualizer/graphs/total.png')
            self.add_graph(scroll_layout, f'visualizer/graphs/{int(month[-1])}month_calendar.png')

            # Add Buttons for Monthly and Weekly Graphs
            self.add_button(scroll_layout, "Bar plots", self.show_bar)
            self.add_button(scroll_layout, "Consuption Calendars", self.show_calendar)
            self.add_button(scroll_layout, "Weekly Graphs", self.show_weekly)
            self.add_button(scroll_layout, "Monthly Graphs", self.show_monthly)

        except Exception as e:
            no_data_label = Label(
                text="Unable to visualize.",
                size_hint_y=None,
                height=30,
                font_size='16sp'
            )
            print(f"Error code: {str(e)}")
            scroll_layout.add_widget(no_data_label)

        scroll_view.add_widget(scroll_layout)
        layout.add_widget(scroll_view)

        return layout

    def add_graph(self, layout, source):
        graph_box = BoxLayout(orientation='vertical', size_hint_y=None, height=700)
        img_widget = Image(source=source, allow_stretch=True)
        img_widget.bind(on_touch_down=self.show_image_popup)
        graph_box.add_widget(img_widget)
        layout.add_widget(graph_box)

    def add_button(self, layout, text, callback):
        button_box = BoxLayout(orientation='vertical', size_hint_y=None, height=60)
        button = Button(
            text=text,
            font_size=20,
            size_hint=(1, None),
            height=50
        )
        button.bind(on_press=callback)
        button_box.add_widget(button)
        layout.add_widget(button_box)

    def show_monthly(self, instance):
        visualizer.monthly_gen()
        popup = Show_monthly(file_path="data_csv/data.csv")
        popup.open()

    def show_weekly(self, instance):
        visualizer.weekly_gen()
        popup = Show_weekly(file_path="data_csv/data.csv")
        popup.open()

    def show_calendar(self, instance):
        popup = Show_calendar(file_path="data_csv/data.csv")
        popup.open()

    def show_bar(self, instance):
        
        popup = Show_bar(file_path="data_csv/data.csv")
        popup.open()

    def show_image_popup(self, instance, touch):
        if instance.collide_point(*touch.pos):
            image_widget = Image(
                source=instance.source,
                allow_stretch=True,
                size_hint=(None, None),
                width=800,
                height=600,
                pos_hint={'center_x': 2, 'center_y': 0.5}
            )
            with image_widget.canvas.before:
                rotate = Rotate(angle=-90, origin=image_widget.center)
                image_widget._rotate_transform = rotate
            
            popup = Popup(
                title="Graph Preview",
                size_hint=(0.9, 0.9)
            )
            popup.content = image_widget
            popup.open()


class Show_monthly(Popup):
    def __init__(self, file_path, **kwargs):
        super().__init__(**kwargs)
        self.title = "Monthly Graphs"
        self.size_hint = (1, 1)
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
                self.add_graph(scroll_layout, f'visualizer/graphs/{len(set(month)) - i}monthly.png')

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

    def add_graph(self, layout, source):
        graph_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=700)
        img_widget = Image(source=source, allow_stretch=True)
        img_widget.bind(on_touch_down=self.show_image_popup)
        graph_box.add_widget(img_widget)
        layout.add_widget(graph_box)

    def show_image_popup(self, instance, touch):
        if instance.collide_point(*touch.pos):
            image_widget = Image(
                source=instance.source,
                allow_stretch=True,
                size_hint=(None, None),
                width=800,
                height=600
            )
            with image_widget.canvas.before:
                rotate = Rotate(angle=-90, origin=image_widget.center)
                image_widget._rotate_transform = rotate
            
            popup = Popup(
                title="Graph Preview",
                size_hint=(0.9, 0.9)
            )
            popup.content = image_widget
            popup.open()


class Show_weekly(Popup):
    def __init__(self, file_path, **kwargs):
        super().__init__(**kwargs)
        self.title = "Weekly Graphs"
        self.size_hint = (1, 1)
        self.file_path = file_path
        self.content = self.show_graphs()

    def show_graphs(self):
        layout = BoxLayout(orientation='vertical', spacing=10)
        scroll_view = ScrollView(size_hint=(1, 1), do_scroll_x=False)
        scroll_layout = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None)
        scroll_layout.bind(minimum_height=scroll_layout.setter('height'))

        try:
            for i in range(4):
                self.add_graph(scroll_layout, f'visualizer/graphs/{3 - i}week.png')

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

    def add_graph(self, layout, source):
        graph_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=700)
        img_widget = Image(source=source, allow_stretch=True)
        img_widget.bind(on_touch_down=self.show_image_popup)
        graph_box.add_widget(img_widget)
        layout.add_widget(graph_box)

    def show_image_popup(self, instance, touch):
        if instance.collide_point(*touch.pos):
            image_widget = Image(
                source=instance.source,
                allow_stretch=True,
                size_hint=(None, None),
                width=800,
                height=600
            )
            with image_widget.canvas.before:
                rotate = Rotate(angle=-90, origin=image_widget.center)
                image_widget._rotate_transform = rotate
            
            popup = Popup(
                title="Graph Preview",
                size_hint=(0.9, 0.9)
            )
            popup.content = image_widget
            popup.open()

class Show_calendar(Popup):
    def __init__(self, file_path, **kwargs):
        super().__init__(**kwargs)
        self.title = "Consuption Calendars"
        self.size_hint = (1, 1)
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
                self.add_graph(scroll_layout, f'visualizer/graphs/{len(set(month)) - i}month_calendar.png')

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

    def add_graph(self, layout, source):
        graph_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=700)
        img_widget = Image(source=source, allow_stretch=True)
        img_widget.bind(on_touch_down=self.show_image_popup)
        graph_box.add_widget(img_widget)
        layout.add_widget(graph_box)

    def show_image_popup(self, instance, touch):
        if instance.collide_point(*touch.pos):
            image_widget = Image(
                source=instance.source,
                allow_stretch=True,
                size_hint=(None, None),
                width=800,
                height=600
            )
            with image_widget.canvas.before:
                rotate = Rotate(angle=-90, origin=image_widget.center)
                image_widget._rotate_transform = rotate
            
            popup = Popup(
                title="Graph Preview",
                size_hint=(0.9, 0.9)
            )
            popup.content = image_widget
            popup.open()


class Show_bar(Popup):
    def __init__(self, file_path, **kwargs):
        super().__init__(**kwargs)
        self.title = "Bar plots"
        self.size_hint = (1, 1)
        self.file_path = file_path
        self.content = self.show_graphs()

    def show_graphs(self):
        date, note, amount, total_amount = data_csv.read_data(self.file_path)
        ymd, hnm, sec = data_csv.time_seper(date)
        year, month, day = data_csv.day_seper(ymd)
        plots_li = visualizer.bar_total()

        layout = BoxLayout(orientation='vertical', spacing=10)
        scroll_view = ScrollView(size_hint=(1, 1), do_scroll_x=False)
        scroll_layout = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None)
        scroll_layout.bind(minimum_height=scroll_layout.setter('height'))

        try:
            for names in plots_li:
                self.add_graph(scroll_layout, f'visualizer/graphs/{names}')

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

    def add_graph(self, layout, source):
        graph_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=700)
        img_widget = Image(source=source, allow_stretch=True)
        img_widget.bind(on_touch_down=self.show_image_popup)
        graph_box.add_widget(img_widget)
        layout.add_widget(graph_box)

    def show_image_popup(self, instance, touch):
        if instance.collide_point(*touch.pos):
            image_widget = Image(
                source=instance.source,
                allow_stretch=True,
                size_hint=(None, None),
                width=800,
                height=600
            )
            with image_widget.canvas.before:
                rotate = Rotate(angle=-90, origin=image_widget.center)
                image_widget._rotate_transform = rotate
            
            popup = Popup(
                title="Graph Preview",
                size_hint=(0.9, 0.9)
            )
            popup.content = image_widget
            popup.open()