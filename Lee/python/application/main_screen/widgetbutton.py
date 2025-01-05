from kivy.uix.button import Button

import widgets

class WidgetButton(Button):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "Widgets"
        self.size_hint = (None, None)
        self.size = (100, 50)
        self.pos = (10, 10)
        self.bind(on_press=self.show_widgets)

    def show_widgets(self, instance):
        popup = widgets.WidgetPopup()
        popup.open()