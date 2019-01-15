import sqlite3 as sql


# work with functions
def create_table():
    conn = sql.connect('lite.db')
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()

def insert_data(item, quantity, price):
    conn = sql.connect('lite.db')
    cur=conn.cursor()
    # don't pass directly the variables into the VALUES fields. Could be potential security risk - sql injection
    # instead pass question marks (act as placeholders) and then list the variables at the end
    cur.execute('INSERT INTO store VALUES (?,?,?)',(item, quantity,price))
    conn.commit()
    conn.close()

def view_data():
    conn = sql.connect('lite.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM store')
    rows=cur.fetchall()
    conn.close()
    return rows

def delete_data(item):
    conn = sql.connect('lite.db')
    cur=conn.cursor()
    cur.execute('DELETE FROM store WHERE item=?',(item,))
    # if error: sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 9 supplied.
    # remember to add the comma after item, in the list of parms (only needed when you have single parm passed)
    conn.commit()
    conn.close()

def update_data(quantity, price, item):
    conn = sql.connect('lite.db')
    cur=conn.cursor()
    cur.execute('UPDATE store SET quantity=?, price=? WHERE item=?',(quantity, price,item))
    conn.commit()
    conn.close()

print(view_data())
delete_data('Coffe cup')
print(view_data())
update_data(30,3.5,'Water glass')
print(view_data())
