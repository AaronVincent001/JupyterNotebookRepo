import sqlalchemy as sa

# Create the engine to connect to the existing SQLite database
engine = sa.create_engine('sqlite:///books.db')

# Connect and execute the raw SQL query
with engine.connect() as conn:
    sql = sa.text('select title from book order by title asc')
    for row in conn.execute(sql):
        print(row[0])
