#!/home/galesky/Documents/GitHub/aaesongie/Lee/python/application/kivy_venv/bin/python3.10

from kivy.config import Config

# Config.set('graphics', 'width', '800')
# Config.set('graphics', 'height', '1500')
# Config.set('graphics', 'resizable', True)


from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.storage.jsonstore import JsonStore
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.graphics import Color, Rectangle



import main_screen


kor_font = 'NanumGothicBold.ttf'

# Define your UI class
class Every_Bank_setting(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Initialize the store
        self.store = JsonStore('data.json')

        # UI setup
        self.initialize_ui()

    def initialize_ui(self):
        # Widget Menu Button (with Material Design)
        widget_button = main_screen.WidgetButton()
        self.add_widget(widget_button)

        # Background Image
        background = Image(source='khu.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(background)

        # # Input Layout (with custom styling)
        input_layout = main_screen.InputLayout()
        self.add_widget(input_layout)

        # Save Button (with Material Design)
        save_button = main_screen.SaveButton(self.store, input_layout.money_input, 
                                             input_layout.note_input)
        self.add_widget(save_button)



class Every_Bank(MDApp):
    def build(self):
        return Every_Bank_setting()


if __name__ == "__main__":
    Every_Bank().run()
