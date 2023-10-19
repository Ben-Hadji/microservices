import psycopg2

conn = psycopg2.connect(database="ben_flask", user="postgres", password="Benhadji99", port="5432")
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS types (id serial PRIMARY KEY, name varchar(100))''')
cur.execute('''CREATE TABLE IF NOT EXISTS items (id serial PRIMARY KEY, name varchar(100), price float, type_id integer REFERENCES types(id))''')

cur.execute('''INSERT INTO types (name) VALUES ('school'), ('office')''')
cur.execute('''INSERT INTO items (name, price, type_id) VALUES ('pen', 1.99, 1), ('pencil', 0.99, 1), ('paper', 2.99, 1), ('stapler', 5.99, 2), ('staples', 0.99, 2)''')

conn.commit()
cur.close()
conn.close()