import sqlite3

# 데이터베이스 초기화
def init_db():
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            date TEXT DEFAULT CURRENT_TIMESTAMP,
            amount REAL,
            note TEXT
        )
    ''')
    conn.commit()
    conn.close()

# 데이터베이스에 거래 정보 추가
def db_add_transaction(amount, note):
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO transactions (amount, note) VALUES (?, ?)
    ''', (amount, note))
    conn.commit()
    conn.close()

# 데이터베이스에서 거래 기록 가져오기
def db_get_transactions():
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('SELECT * FROM transactions')
    rows = c.fetchall()
    conn.close()
    return rows

def db_delete_transaction(transaction_id):
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('''
        DELETE FROM transactions WHERE id = ?
    ''', (transaction_id,))
    conn.commit()
    conn.close()