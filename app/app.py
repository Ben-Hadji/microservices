import time
import psycopg2
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def db_conn():
    conn = psycopg2.connect(host='flask_db', user="postgres", password="Benhadji99", port="5432")
    return conn

@app.route('/', methods=['GET']) # on définit la route pour la page d'accueil
def index():
    conn = db_conn() # on se connecte à la base de données
    cur = conn.cursor() # on crée un curseur pour exécuter nos requêtes
    cur.execute('''SELECT * FROM items ORDER BY name''') # on exécute une requête SQL pour récupérer tous les items
    items = cur.fetchall() # on récupère tous les résultats de la requête et on les stocke dans la variable 'items'
    cur.execute('''SELECT * FROM types''') # on exécute une requête SQL pour récupérer tous les types
    types = cur.fetchall() # on récupère tous les résultats de la requête et on les stocke dans la variable 'types'
    cur.close() # on ferme le curseur
    conn.close() # on ferme la connexion à la base de données
    return render_template('index.html', items=items, types=types) # on affiche le template 'index.html' avec les variables 'items' et 'types'



@app.route('/add_item', methods=['POST']) # on définit la route pour ajouter un item
def create():
    conn = db_conn()
    cur = conn.cursor()
    name = request.form['name'] # on récupère le nom de l'item via le formulaire
    price = request.form['price'] # on récupère le prix de l'item via le formulaire
    type_id = request.form['type_id'] # on récupère l'id du type de l'item via le formulaire
    cur.execute('''INSERT INTO items (name, price, type_id) VALUES (%s, %s, %s)''', (name, price, type_id)) # on insère l'item dans la table
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index')) # on redirige vers la page d'accueil

@app.route('/update', methods=['POST']) # on définit la route pour modifier un item
def update():
    conn = db_conn()
    cur = conn.cursor()
    id = request.form['id']
    name = request.form['name']
    price = request.form['price']
    type_id = request.form['type_id']
    cur.execute('''UPDATE items SET name=%s, price=%s, type_id=%s WHERE id=%s''', (name, price, type_id, id)) # 
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    conn = db_conn()
    cur = conn.cursor()
    id = request.form['id'] # get the id of the item to delete
    cur.execute('''DELETE FROM items WHERE id=%s''', (id,)) # delete the item
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index')) # redirect to the home page

if __name__ == '__main__':
    time.sleep(10)
    app.run(host="0.0.0.0",port=5000)