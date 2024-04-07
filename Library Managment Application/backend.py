import sqlite3


def create_table():
    conn = sqlite3.connect('lite_1.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Books (Title TEXT,Year INT, Author TEXT,ISBN INT)")
    conn.commit()
    conn.close()


def add_entry(title, year, author, isbn):
    conn = sqlite3.connect('lite_1.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Books VALUES (?,?,?,?)", (title, year, author, isbn))
    conn.commit()
    conn.close()


def view_entries():
    conn = sqlite3.connect('lite_1.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Books')
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_entry()

