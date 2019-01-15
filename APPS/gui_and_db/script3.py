import psycopg2 as pg2


# work with functions
def create_table():
    conn = pg2.connect("dbname='db1' user='postgres' password='postgres' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()

def insert_data(item, quantity, price):
    conn = pg2.connect("dbname='db1' user='postgres' password='postgres' host='localhost' port='5432'")
    cur=conn.cursor()
    # for postgresql, we can use string formatting placeholders (instead of ? from sqlite3)
    # cur.execute('INSERT INTO store VALUES ('%s','%s','%s')' %(item, quantity, price))    # this is prone to sql injection as well
    cur.execute('INSERT INTO store VALUES (%s,%s,%s)', (item, quantity, price))
    conn.commit()
    conn.close()

def view_data():
    conn = pg2.connect("dbname='db1' user='postgres' password='postgres' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute('SELECT * FROM store')
    rows=cur.fetchall()
    conn.close()
    return rows

def delete_data(item):
    conn = pg2.connect("dbname='db1' user='postgres' password='postgres' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute('DELETE FROM store WHERE item=%s',(item,))
    # if error: pg2ite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 9 supplied.
    # remember to add the comma after item, in the list of parms (only needed when you have single parm passed)
    conn.commit()
    conn.close()

def update_data(quantity, price, item):
    conn = pg2.connect("dbname='db1' user='postgres' password='postgres' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute('UPDATE store SET quantity=%s, price=%s WHERE item=%s',(quantity, price,item))
    conn.commit()
    conn.close()


# create_table()
# insert_data("Orange", 20, 1)
# print(view_data())
# delete_data('Orange')
print(view_data())
update_data(10, 2.5, 'Apple')
print(view_data())
