#!/home/galesky/Documents/GitHub/aaesongie/Lee/python/application/kivy_venv/bin/python3.10

kor_font = 'NanumGothicBold.ttf'

from kivy.lang import Builder
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivymd.app import MDApp

import os

import main_screen
import data_csv
import Initial_screen


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # MainScreen의 레이아웃 추가
        layout = Every_Bank_setting()
        self.add_widget(layout)


class Every_Bank_setting(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Initialize the file_path
        self.file_path = 'data_csv/data.csv'

        # UI setup
        self.initialize_ui()

    def initialize_ui(self):
        # Widget Menu Button (with Material Design)
        widget_button = main_screen.WidgetButton()
        self.add_widget(widget_button)

        # Background Image
        background = Image(source='khu.png', allow_stretch=False, keep_ratio=True)
        self.add_widget(background)

        # Input Layout (with custom styling)
        input_layout = main_screen.InputLayout()
        self.add_widget(input_layout)

        # Save Button (with Material Design)
        save_button = main_screen.SaveButton(self.file_path, input_layout.money_input, 
                                             input_layout.note_input)
        self.add_widget(save_button)


class Every_Bank(MDApp):
    def build(self):
        # ScreenManager 생성
        sm = ScreenManager()

        # Initialize x to 0
        self.x = 0

        # Create the WelcomeScreen initially
        self.initial_screen = Initial_screen.InitialScreen(name="Initial")
        sm.add_widget(self.initial_screen)

        # Schedule the function to check `change` after 0.5 seconds
        Clock.schedule_interval(self.check_change_value, 0.5)

        return sm

    def check_change_value(self, dt):
        # If `change` in InitialScreen is 1, switch to the MainScreen
        if self.initial_screen.change == 1:
            sm = self.root  # Access the ScreenManager
            sm.clear_widgets()  # Clear all current screens
            sm.add_widget(MainScreen(name="main"))  # Add MainScreen
            sm.current = "main"  # Switch to MainScreen
            return False  # Stop the clock from continuing to check

if __name__ == "__main__":
    Every_Bank().run()
