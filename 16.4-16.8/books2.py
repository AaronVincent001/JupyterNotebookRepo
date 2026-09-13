import csv
import sqlite3

db = sqlite3.connect('books.db')
curs = db.cursor()

ins_str = 'insert into book values(?, ?, ?)'

with open('books2.csv', 'rt') as infile:
    books = csv.DictReader(infile)
    for book in books:
        curs.execute(ins_str, (book['title'], book['author'], book['year']))

db.commit()
