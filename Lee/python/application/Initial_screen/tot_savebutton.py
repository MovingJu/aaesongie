from kivy.uix.button import Button
import data_csv

class TotalSaveButton(Button):


    def __init__(self, file_path, total_amount, **kwargs):
        super().__init__(**kwargs)
        self.text = "Save"
        self.size_hint_y = None
        self.height = 50
        
        self.file_path = file_path
        self.total_amount = total_amount
        self.tot_pressed = 0  # Initial value
        
        # Bind the on_press event to a method
        self.bind(on_press=self.on_button_press)

    def on_button_press(self, instance):


        ##### 이 기능 추가해야함.
        data_csv.save_initial_data(self.file_path, self.total_amount)
        
        # Update the tot_pressed value
        self.tot_pressed = 1
