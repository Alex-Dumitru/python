import sqlite3 as sql


# create a connection
# if the db file doesn't exist, it will be created automatically and connect to it
conn = sql.connect('lite.db')

# create a cursor object
cur=conn.cursor()

# sql queries # it is good to write the SQL statements in CAPITAL letters
#cur.execute('CREATE TABLE store (item TEXT, quantity INTEGER, price REAL)')
# it's good to have and IF statement, in case the TABLE already exists, so if we run the program multiple times, we will not get any errors
cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')


# adding data
cur.execute('INSERT INTO store VALUES ("Wine Glass", 8, 10.5)')
# commit the changes to the db
conn.commit()

# close the connection
conn.close()
