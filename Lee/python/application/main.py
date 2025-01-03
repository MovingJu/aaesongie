from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import sqlite3


class ExpenseTracker(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # 입력 필드
        self.date_input = TextInput(hint_text="Enter Date (YYYY-MM-DD)", multiline=False)
        self.category_input = TextInput(hint_text="Enter Category (e.g., Food, Rent)", multiline=False)
        self.amount_input = TextInput(hint_text="Enter Amount", multiline=False, input_filter='float')
        self.note_input = TextInput(hint_text="Enter Note (Optional)", multiline=False)

        self.add_widget(self.date_input)
        self.add_widget(self.category_input)
        self.add_widget(self.amount_input)
        self.add_widget(self.note_input)

        # 버튼
        self.add_button = Button(text="Add Expense", on_press=self.add_expense)
        self.view_button = Button(text="View Records", on_press=self.view_records)

        self.add_widget(self.add_button)
        self.add_widget(self.view_button)

        # 결과 표시
        self.result_label = Label(text="")
        self.add_widget(self.result_label)

        # DB 초기화
        self.init_db()

    def init_db(self):
        self.conn = sqlite3.connect("expenses.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                date TEXT,
                category TEXT,
                amount REAL,
                note TEXT
            )
        """)
        self.conn.commit()

    def add_expense(self, instance):
        # 데이터 추가
        date = self.date_input.text
        category = self.category_input.text
        amount = self.amount_input.text
        note = self.note_input.text

        if not date or not category or not amount:
            self.result_label.text = "Please fill all required fields."
            return

        try:
            self.cursor.execute("INSERT INTO transactions (date, category, amount, note) VALUES (?, ?, ?, ?)",
                                (date, category, float(amount), note))
            self.conn.commit()
            self.result_label.text = "Expense added successfully!"
            self.clear_inputs()
        except Exception as e:
            self.result_label.text = f"Error: {e}"

    def view_records(self, instance):
        # 데이터 보기
        self.cursor.execute("SELECT * FROM transactions")
        records = self.cursor.fetchall()
        if records:
            self.result_label.text = "\n".join([f"{r[1]} - {r[2]}: ${r[3]} ({r[4]})" for r in records])
        else:
            self.result_label.text = "No records found."

    def clear_inputs(self):
        self.date_input.text = ""
        self.category_input.text = ""
        self.amount_input.text = ""
        self.note_input.text = ""


class ExpenseTrackerApp(App):
    def build(self):
        return ExpenseTracker()


if __name__ == "__main__":
    ExpenseTrackerApp().run()
