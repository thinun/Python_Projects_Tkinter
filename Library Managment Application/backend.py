import sqlite3


def create_table():
    conn = sqlite3.connect('lite_1.db')
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT,year INTEGER, author TEXT,isbn INTEGER)")
    conn.commit()
    conn.close()


def add_entry(title, year, author, isbn):
    conn = sqlite3.connect('lite_1.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title, year, author, isbn))
    conn.commit()
    conn.close()


def view_entries():
    conn = sqlite3.connect('lite_1.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    rows = cursor.fetchall()
    conn.close()
    return rows


def search_entry(title='', year='', author='', isbn=''):
    conn = sqlite3.connect('lite_1.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title=? OR year=? OR author=? OR isbn=?", (title, year, author, isbn))
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete_entry(id):
    conn = sqlite3.connect('lite_1.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update_entry(id, title, year, author, isbn):
    conn = sqlite3.connect('lite_1.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title=?, year=?, author=?, isbn=? WHERE id=?", (title, year, author, isbn, id))
    conn.commit()
    conn.close()


