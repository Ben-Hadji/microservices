import psycopg2

conn = psycopg2.connect(database="ben_flask", user="postgres", password="Benhadji99", port="5432")
cur = conn.cursor()

# Création de la table 'type'
cur.execute('''
    CREATE TABLE IF NOT EXISTS type (
        id serial PRIMARY KEY,
        name varchar(100)
    )
''')

# Création de la table 'items'
cur.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id serial PRIMARY KEY,
        name varchar(100),
        price float
    )
''')

# Création de la table de jointure 'item_type' pour gérer les associations many-to-many
cur.execute('''
    CREATE TABLE IF NOT EXISTS item_type (
        id serial PRIMARY KEY,
        item_id int REFERENCES items(id),
        type_id int REFERENCES type(id)
    )
''')

# Insertion de types
cur.execute("INSERT INTO type (name) VALUES ('Type A'), ('Type B')")

# Insertion d'items
cur.execute("INSERT INTO items (name, price) VALUES ('pen', 0.99), ('pencil', 0.50), ('eraser', 0.25)")

# Insertion d'associations entre items et types dans la table de jointure 'item_type'
cur.execute("INSERT INTO item_type (item_id, type_id) VALUES (1, 1), (2, 1), (3, 2), (1, 2)")

conn.commit()

cur.close()
conn.close()
