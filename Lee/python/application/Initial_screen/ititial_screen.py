from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout

from .tot_input_layout import InputLayout
from .tot_savebutton import TotalSaveButton
import main_screen


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

        self.orientation = 'vertical'
        content_layout = BoxLayout(orientation='vertical', size_hint=(1, 1))

        content_layout.spacing = dp(10)
        content_layout.padding = dp(50)  # Padding to adjust the spacing from the screen edges

        widget_button = main_screen.WidgetButton()
        widget_button.opacity = 0
        content_layout.add_widget(widget_button)

        # Background Image (adjust size_hint for proper sizing)
        background = Image(source='khu.png', allow_stretch=False, keep_ratio=True)
        content_layout.add_widget(background)

        # Spacer to adjust the space between background image and input fields
        spacer = Widget(size_hint_y=None, height=dp(100))  # Adjust the height for spacing between the image and input fields
        content_layout.add_widget(spacer)

        # Input Layout
        input_layout = InputLayout()
        content_layout.add_widget(input_layout)

        # Save Button
        save_button = TotalSaveButton(self.file_path, input_layout.total_amount)
        content_layout.add_widget(save_button)

        # Bind the button press to the function that will update the change value
        save_button.bind(on_press=self.on_save_button_press)

        # Add the content_layout (which contains both the image and input fields) to the screen
        self.add_widget(content_layout)

    def on_save_button_press(self, instance):
        # When the save button is pressed, set self.change to 1
        self.change = 1
