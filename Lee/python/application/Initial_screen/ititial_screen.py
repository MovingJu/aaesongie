from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.label import Label

from .tot_input_layout import InputLayout
from .tot_savebutton import TotalSaveButton


class InitialScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Initialize the file_path
        self.file_path = 'data_csv/data.csv'

        # Initialize the change value
        self.change = 0  # Default value is 0

        # UI setup
        self.initialize_ui()

    def initialize_ui(self):
        # Background Image
        background = Image(source='khu.png', allow_stretch=False, keep_ratio=True)
        self.add_widget(background)

        # Input Layout
        input_layout = InputLayout()
        self.add_widget(input_layout)

        # Save Button
        save_button = TotalSaveButton(self.file_path, input_layout.total_amount)
        self.add_widget(save_button)

        # Bind the button press to the function that will update the change value
        save_button.bind(on_press=self.on_save_button_press)

    def on_save_button_press(self, instance):
        # When the save button is pressed, set self.change to 1
        self.change = 1
