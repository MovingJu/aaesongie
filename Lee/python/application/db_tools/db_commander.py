from .db_manage import *

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.button import Button

class Transaction():

    def add_transaction(self, instance):
        amount = self.amount_input.text
        note = self.note_input.text

        if amount:
            db_add_transaction(float(amount), note)
            self.amount_input.text = ""
            self.note_input.text = ""
            self.show_popup("Transaction Added", f"Amount: {amount}\nNote: {note}")
        else:
            self.show_popup("Error", "Amount is required.")


    def delete_transaction(self, transaction_id, reload_popup):
        # Assuming you have logic for deleting the transaction from the database
        db_delete_transaction(transaction_id)

        # After deletion, reload the popup
        reload_popup()

    def show_popup(self, title, message):
        # Implement the show_popup method for displaying popups
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.8))
        popup.open()
