import sqlite3

def create_table():
    conn = sqlite3.connect('lite_1.db')
    cursor = conn.cursor()
    conn.execute("CREATE TABLE IF NOT EXISTS Books (Title TEXT,Year INT, Author TEXT,ISBN INT)")
    conn.commit()
    conn.close()



def add_entry(title, year, author, isbn):
    conn = sqlite3.connect('lite_1.db')
    cursor = conn.cursor()
    conn.execute("INSERT INTO Books VALUES (?,?,?,?)", (title, year, author, isbn))
    conn.commit()
    conn.close()



def view_entries():
    conn = sqlite3.connect('lite_1.db')
    cursor = conn.cursor()
    conn.execute('SELECT * FROM Books')
    rows = cursor.fetchall()
    conn.close()
    return rows

create_table()
#add_entry('Lord of the Ring 1', '2009', 'thinun', '223245')
#add_entry('Lord of the Ring 2', '2010', 'thinun',223246)

print(view_entries())