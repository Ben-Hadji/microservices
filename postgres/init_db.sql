-- Création de la table "types" avec une séquence "id" et un champ "name"
CREATE TABLE IF NOT EXISTS types (
    id serial PRIMARY KEY,
    name varchar(100)
);

-- Création de la table "items" avec une séquence "id" et des champs "name", "price" et "type_id" avec une contrainte de clé étrangère
CREATE TABLE IF NOT EXISTS items (
    id serial PRIMARY KEY,
    name varchar(100),
    price float,
    type_id integer REFERENCES types(id)
);

-- Insertion de données dans la table "types"
INSERT INTO types (name) VALUES ('school'), ('office');

-- Insertion de données dans la table "items"
INSERT INTO items (name, price, type_id) VALUES
    ('pen', 1.99, 1),
    ('pencil', 0.99, 1),
    ('paper', 2.99, 1),
    ('stapler', 5.99, 2),
    ('staples', 0.99, 2);
