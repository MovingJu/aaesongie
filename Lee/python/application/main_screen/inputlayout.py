from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.metrics import dp


class InputLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = dp(100)
        self.padding = dp(0)

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
        self.money_input.bind(on_text_validate=self.on_amount_enter, text=self.on_amount_change)
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
        self.add_widget(self.note_input)

        # Spacer for layout alignment
        self.spacer = Widget(size_hint_y=None, height=dp(10))
        self.add_widget(self.spacer)

    def on_amount_enter(self, instance):
        """Amount 입력 완료 시 호출."""
        value = self.money_input.text.strip()
        if value:  # Amount 입력 완료 시 Note 필드 표시 및 위치 변경
            self.show_note_input()
            self.swap_inputs()

    def on_amount_change(self, instance, value):
        """Amount 입력 변화에 반응."""
        if not value.strip():  # Amount 입력이 없으면 초기 상태로 복구
            if self.note_visible:
                self.reset_layout()

    def show_note_input(self):
        """Note 입력 필드를 활성화."""
        self.note_input.opacity = 1
        self.note_input.disabled = False
        self.note_visible = True

    def hide_note_input(self):
        """Note 입력 필드를 비활성화."""
        self.note_input.opacity = 0
        self.note_input.disabled = True
        self.note_visible = False

    def swap_inputs(self):
        """money_input과 note_input 위치를 교환."""
        self.clear_widgets()  # 기존 위젯들을 제거
        # Note 필드를 먼저 추가하여 순서를 변경
        self.add_widget(self.note_input)
        self.add_widget(self.money_input)
        self.add_widget(self.spacer)

    def reset_layout(self):
        """원래 상태로 레이아웃 복구."""
        self.clear_widgets()  # 기존 위젯들을 제거
        # Amount 필드를 먼저 추가하여 순서를 복구
        self.add_widget(self.money_input)
        self.add_widget(self.note_input)
        self.add_widget(self.spacer)
        self.hide_note_input()  # Note 필드 숨김

    def reset_layout(self):
        """원래 상태로 레이아웃 복구."""
        self.money_input.text = ""  # Amount 필드 초기화
        self.note_input.text = ""   # Note 필드 초기화
        self.clear_widgets()        # 기존 위젯들을 제거
        # Amount 필드를 먼저 추가하여 순서를 복구
        self.add_widget(self.money_input)
        self.add_widget(self.note_input)
        self.add_widget(self.spacer)
        self.hide_note_input()      # Note 필드 숨김
