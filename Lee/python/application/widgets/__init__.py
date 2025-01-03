from .transaction_list import Transaction_list


from kivy.uix.button import Button

class Widgets():

    def show_widgets(self, instance):
        self.popup_content.clear_widgets()
        self.popup_content.add_widget(Button(text="Widget 1", font_size=32, height=80))
        self.popup_content.add_widget(Button(text="Widget 2", font_size=32, height=80))
        self.popup_content.add_widget(Button(text="Widget 3", font_size=32, height=80))
        self.popup.open()