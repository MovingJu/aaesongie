from kivy.uix.button import Button

import data_json

class SaveButton(Button):

    save_data = data_json.save_data

    def __init__(self, store, money_input, note_input, **kwargs):
        super().__init__(**kwargs)
        self.text = "Save"
        self.size_hint_y = None
        self.height = 50
        
        self.bind(on_press=self.save_data)
        self.store = store
        self.money_input = money_input
        self.note_input = note_input
