import os
import sqlite3
import pytest
from pytestqt import qtbot
from main import UserApp

def test_add_user(qtbot):
    test_db = "test_users.db"
    if os.path.exists(test_db):
        os.remove(test_db)
    
    conn = sqlite3.connect(test_db)
    conn.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )''')
    conn.close()
    
    app = UserApp() 
    app.db.conn = sqlite3.connect(test_db)
    app.db.cursor = app.db.conn.cursor()
    qtbot.addWidget(app)
    
    app.db.add_user("Usuario1", "1234", "Usuari")
    app.load_users()
    assert app.table.rowCount() == 1
    
    app.close()
    os.remove(test_db)