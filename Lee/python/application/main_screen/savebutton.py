from kivy.uix.button import Button

import data_csv

class SaveButton(Button):

    save_data = data_csv.save_data

    def __init__(self, file_path, money_input, note_input, **kwargs):
        super().__init__(**kwargs)
        self.text = "Save"
        self.size_hint_y = None
        self.height = 50
        
        self.file_path = file_path
        self.money_input = money_input
        self.note_input = note_input

        self.bind(on_press=self.save_data)