import sqlite3

def connection():
    conn = sqlite3.connect("base.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT,quntity INTEGER,price REAL)")
    conn.commit()
    conn.close()

def insert(item,quntity,price):
    conn = sqlite3.connect("base.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quntity,price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("base.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return  rows

def delete(item):
    conn = sqlite3.connect("base.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(item,quntity,price):
    conn = sqlite3.connect("base.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quntity=? , price=? WHERE item=?",(quntity,price,item))
    conn.commit()
    conn.close()

# insert("Coffe Cup",8,18.5)
update("Coffe Cup",200,1500.45)
# delete("Rose Glass")
print(view())