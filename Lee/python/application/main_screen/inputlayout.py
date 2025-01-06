from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.metrics import dp


class InputLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = dp(100)
        self.padding = dp(50)

        # Note 입력 필드 표시 여부
        self.note_visible = False

        # Amount 입력 필드
        self.money_input = TextInput(
            hint_text="Enter Amount (e.g., 10000)",
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
        self.money_input.bind(text=self.on_amount_text)  # 입력 이벤트 연결
        self.add_widget(self.money_input)

        # Note 입력 필드 (초기화는 하지만 숨김 상태)
        self.note_input = TextInput(
            hint_text="Enter Note (e.g., Coffee, Rent)",
            font_name='NanumGothicBold.ttf',
            multiline=False,
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1),
            padding=(10, 10),
            font_size="16sp",
            size_hint_y=None,
            height=dp(40),
            opacity=0,  # 보이지 않도록 설정
            disabled=True  # 비활성화 상태로 설정
        )
        self.add_widget(self.note_input)  # 초기에는 보이지 않지만 레이아웃에 추가

        # Spacer for layout alignment
        self.add_widget(Widget(size_hint_y=None, height=dp(10)))

    def on_amount_text(self, instance, value):
        """Amount 입력 변화에 반응."""
        if value.strip():  # Amount 입력 시 Note 필드 표시
            if not self.note_visible:
                self.show_note_input()
                self.note_visible = True
        else:  # Amount 입력이 없으면 Note 필드 숨김
            if self.note_visible:
                self.hide_note_input()
                self.note_visible = False

    def show_note_input(self):
        """Note 입력 필드를 활성화."""
        self.note_input.opacity = 1
        self.note_input.disabled = False

    def hide_note_input(self):
        """Note 입력 필드를 비활성화."""
        self.note_input.opacity = 0
        self.note_input.disabled = True
