# sql lite is portable database its data stored in a .db file
# when working with data bases
# 1st connect to the data base
# 2nd create a cursor object
# 3rd Write an SQL query
# 4th Commit changes
# 5th close the database connection

import sqlite3


def create_table():
    # if i dont have a database file this will auto creat an db file an create a connection
    conn = sqlite3.connect('lite.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER,price REAL)")
    conn.commit()
    conn.close()


def add_item(item, quntity, price):
    conn = sqlite3.connect('lite.db')
    cursor = conn.cursor()
    conn.execute('INSERT INTO store VALUES (?,?,?)', (item, quntity, price))
    conn.commit()
    conn.close()


def show_all_items():
    conn = sqlite3.connect('lite.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_item(item):
    conn = sqlite3.connect('lite.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM store WHERE item=?', (item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = sqlite3.connect('lite.db')
    cursor = conn.cursor()
    conn.execute('UPDATE store SET quantity=?, price=? WHERE item=?', (quantity, price, item))
    conn.commit()
    conn.close()


print(show_all_items())

update(50,10,'apple')
print(show_all_items())