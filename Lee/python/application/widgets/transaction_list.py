from db_tools.db_commander import *

class Transaction_list():

    def view_transactions(self, instance):
        transactions = db_get_transactions()
        content = BoxLayout(orientation='vertical', spacing=10)

        def reload_popup():
            
            popup.dismiss()
           
            self.view_transactions(instance)

        for row in transactions:
            transaction_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            
            label = Label(text=f"Amount: {row[2]}, Note: {row[3]}", font_size=24, size_hint_x=0.8)
            
            # Pass the row[0] (transaction_id) to the lambda function and reload_popup for refreshing
            delete_button = Button(text="Delete", on_press=lambda instance, transaction_id=row[0]: self.delete_transaction(transaction_id, reload_popup), size_hint_x=0.2)
            
            transaction_layout.add_widget(label)
            transaction_layout.add_widget(delete_button)

            content.add_widget(transaction_layout)

        scroll_view = ScrollView()
        scroll_view.add_widget(content)

        popup = Popup(title="Transactions", content=scroll_view, size_hint=(0.8, 0.8))
        popup.open()