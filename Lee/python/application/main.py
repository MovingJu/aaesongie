#!/home/galesky/Documents/GitHub/aaesongie/Lee/python/application/kivymd_venv/bin/python3.10

kor_font = 'NanumGothicBold.ttf'

from kivy.lang import Builder
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.metrics import dp

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

        # content_layout 설정 (배경 이미지와 입력 필드 사이의 간격을 동일하게 적용)
        content_layout = BoxLayout(orientation='vertical', size_hint=(1, 1))
        
        content_layout.spacing = dp(20)  # 배경 이미지와 입력 필드 사이의 간격
        content_layout.padding = dp(50)  # 입력 필드와 버튼 사이의 간격

        # Initialize the file_path
        self.file_path = 'data_csv/data.csv'

        # UI setup
        self.initialize_ui(content_layout)

    def initialize_ui(self, content_layout):
        # Widget Menu Button (with Material Design)
        widget_button = main_screen.WidgetButton()
        content_layout.add_widget(widget_button)

        # Background Image
        background = Image(source='khu.png', allow_stretch=False, keep_ratio=True)
        content_layout.add_widget(background)

        # Spacer for spacing between background and input fields
        spacer = Widget(size_hint_y=None)  # 배경과 입력 필드 사이의 간격을 맞추기 위해 spacer 추가
        content_layout.add_widget(spacer)

        # Input Layout (with custom styling)
        input_layout = main_screen.InputLayout()
        content_layout.add_widget(input_layout)

        # Save Button (with Material Design)
        save_button = main_screen.SaveButton(self.file_path, input_layout.money_input, 
                                             input_layout.note_input)
        content_layout.add_widget(save_button)

        # content_layout을 현재 레이아웃에 추가
        self.add_widget(content_layout)


class Every_Bank(MDApp):
    def build(self):
        # ScreenManager 생성
        sm = ScreenManager()

        if data_csv.is_csv_mt('data_csv/data.csv'):
            self.x = 0
        else:
            self.x = 1

        # Create the WelcomeScreen initially
        self.initial_screen = Initial_screen.InitialScreen(name="Initial")
        sm.add_widget(self.initial_screen)

        Clock.schedule_interval(self.check_change_value, 0)

        return sm

    def check_change_value(self, dt):
        # If `change` in InitialScreen is 1, switch to the MainScreen
        if self.initial_screen.change or self.x == 1:
            sm = self.root  # Access the ScreenManager
            sm.clear_widgets()  # Clear all current screens
            sm.add_widget(MainScreen(name="main"))  # Add MainScreen
            sm.current = "main"  # Switch to MainScreen
            return False  # Stop the clock from continuing to check

if __name__ == "__main__":
    Every_Bank().run()
