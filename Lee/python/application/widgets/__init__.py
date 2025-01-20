from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout as PopupBox
from kivy.uix.button import Button

import visualizer.calendar

from .transactionlist import TransactionList
from .graphs import Graphs

import visualizer

class WidgetPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Widgets"
        self.size_hint = (0.5, 0.5)
        self.content = self.create_widget_content()

    def create_widget_content(self):
        content = PopupBox(orientation='vertical')

        content.add_widget(Button(text="List", font_size=32, height=80, 
                                  on_press=self.show_widget1))
        
        content.add_widget(Button(text="Graphs", font_size=32, height=80,
                                  on_press=self.show_widget2))

        content.add_widget(Button(text="Widget 3", font_size=32, height=80))
        
        return content
    
    def show_widget1(self, instance):
        popup = TransactionList(file_path="data_csv/data.csv")
        popup.open()

    def show_widget2(self, instance):
        visualizer.total_gen()
        visualizer.calendar_gen()
        
        popup = Graphs(file_path="data_csv/data.csv")
        popup.open()