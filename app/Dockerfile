# 
FROM python:3.8

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier requirements.txt dans le conteneur
COPY requirements.txt requirements.txt

# Copiez tous les fichiers de votre application dans le conteneur
COPY . .

# Installez les dépendances à l'aide de pip
RUN pip install -r requirements.txt


EXPOSE 5000

# Commande pour exécuter l'application Flask
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
