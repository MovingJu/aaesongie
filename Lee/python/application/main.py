#!/home/galesky/Documents/GitHub/aaesongie/Lee/python/application/kivy_venv/bin/python3.10

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label

import db_tools

import widgets

# Kivy 앱 UI 구성
class Every_bank(App, widgets.Widgets, db_tools.Transaction, widgets.transaction_list):

    def build(self):
        self.title = 'Every_bank'
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # 돈 입력 필드
        self.amount_input = TextInput(hint_text="Enter amount", multiline=False, input_filter='float', font_size=32, height=50)
        self.layout.add_widget(self.amount_input)

        # 노트 입력 필드
        self.note_input = TextInput(hint_text="Enter note", multiline=True, font_size=32, height=100)
        self.layout.add_widget(self.note_input)

        # 거래 추가 버튼
        add_button = Button(text="Add Transaction", on_press=self.add_transaction, font_size=32, size_hint=(None, None), size=(400, 80))
        self.layout.add_widget(add_button)

        # 거래 목록 보기 버튼
        view_button = Button(text="View Transactions", on_press=self.view_transactions, font_size=32, size_hint=(None, None), size=(400, 80))
        self.layout.add_widget(view_button)

        # 좌측 상단에 위젯 버튼
        widget_button = Button(text="Widgets", size_hint=(None, None), size=(200, 100), on_press=self.show_widgets, font_size=32)
        self.layout.add_widget(widget_button)

        # 위젯 팝업
        self.popup_content = GridLayout(cols=1, padding=10, spacing=10)
        self.popup = Popup(title="Widgets", content=self.popup_content, size_hint=(None, None), size=(800, 800))

        return self.layout


    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message, font_size=24), size_hint=(None, None), size=(600, 300))
        popup.open()

if __name__ == '__main__':
    db_tools.init_db()
    Every_bank().run()
