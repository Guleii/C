import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE user
                    (id String(20) primary key,
                     name Varchar(20), 
                     gender boolean)''')
cursor.rowcount
cursor.close()
conn.commit()
conn.close()

