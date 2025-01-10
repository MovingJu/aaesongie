from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.metrics import dp


class InputLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        # self.spacing = dp(100)
        # self.padding = dp(50)


        # Initial Amount 입력 필드
        self.total_amount = TextInput(
            hint_text="Enter Bank total amount (e.g., 10000)",
            multiline=False,
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1),
            padding=(10, 10),
            font_size="16sp",
            size_hint_y=None,
            height=dp(40),
            input_filter='int',
            input_type='number'
        )
        self.add_widget(self.total_amount)

        self.spacer = Widget(size_hint_y=None, height=dp(200))
        self.add_widget(self.spacer)
