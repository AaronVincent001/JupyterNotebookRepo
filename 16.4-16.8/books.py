import sqlite3

db = sqlite3.connect('books.db')
curs = db.cursor()
# Note: Named the table 'book' to match the queries in 16.5 through 16.8
curs.execute('''create table book (title text, author text, year int)''')
db.commit()

