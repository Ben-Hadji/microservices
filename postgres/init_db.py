import os
import psycopg2
from psycopg2 import Error


try:
    conn = psycopg2.connect(database=os.getenv("DB_HOST"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), port=os.getenv("DB_PORT"))
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS types (id serial PRIMARY KEY, name varchar(100))''')
    cur.execute('''CREATE TABLE IF NOT EXISTS items (id serial PRIMARY KEY, name varchar(100), price float, type_id integer REFERENCES types(id))''')

    cur.execute('''INSERT INTO types (name) SELECT * FROM (VALUES ('school'), ('office')) AS tmp (name) WHERE NOT EXISTS (SELECT name FROM types WHERE name = tmp.name)''')
    cur.execute('''INSERT INTO items (name, price, type_id) SELECT * FROM (VALUES ('pen', 1.99, 1), ('pencil', 0.99, 1), ('paper', 2.99, 1), ('stapler', 5.99, 2), ('staples', 0.99, 2)) AS tmp (name, price, type_id) WHERE NOT EXISTS (SELECT name FROM items WHERE name = tmp.name)''')

    conn.commit()
    cur.close()
    conn.close()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)