# Rapport de Mi-parcours
Bien sûr, vous pouvez mettre en place un système de gestion d'inventaire automatisé en utilisant uniquement Azure Functions pour le traitement des données et Azure Cosmos DB pour le stockage. Voici comment procéder :

## Architecture

<img width="521" alt="image" src="https://github.com/Ben-Hadji/microservices/assets/83819844/59a9aed8-64e9-4bb6-97bb-470c24ecfd77">

**Fonctionnement**
1. l'utilisateur accède à l'interface utilisateur
2. la connexion est établie via le localhost en utilisant le port 5000 pour accéder à l'application flask
3. l'application flask est exposé et s'exécute sur le port 5000
4. l'application flask traite la demande de l'utilisateur. dans le cas où la demande nécessite des données stockées dans la base de données, Flask établit alors une connexion avec la base de données PostgreSQL en passant par le port 5432 (port sur lequel est exposé PostgreSQL)
5. Après avoir reçu les requêtes SQL de la part de Flask, PostgreSQL les exécute et renvoie les résultats à l'application Flask
6. Flask retourne enfin les résultats vers l'interface graphiques pour les afficher à l'utilisateur.

**Choix techniques**

1. **python Flask** : Ce choix a été fait dû au fait en se basant sur plusieurs raisons parmi lesquels :
    1.  ***Sa simplicité*** : en effet flask est un Framework web minimaliste, qui est simple à apprendre, utiliser et maintenir. Ainsi il s's'inscrit parfaitement dans le contexte sur lequel on travail, qui de privilégier la simplicité.
    2. ***Sa flexibilité*** : On a la possibilité de choisir les bibliothèques et outils que nous souhaitons utiliser sans trop de contraintes.
    3. ***Sa prise en charge d'une variété d'extensions complémentaires*** : Il bénéficie d'une bibliothèque d'extension qui offre plusieurs modules complémentaire pour ajouter des fonctionnalités telles que l'authentification, connexion à des base de données et pleines d'autres qui pourront nous être utiles après, si par exemple on souhaite faire évoluer notre application.
2. **PostgreSQL** : cela nous paraissait évident d'utiliser PostgreSQL pour assurer la gestion de notre base de nos données pour divers arguments dont  :
    1. ***Son évolutivité*** : Il est capable de gérer des volumes importants de données et permet d'améliorer la disponibilité des données et la tolérance aux pannes grâce à des fonctionnalités telles que la réplication.
    2. ***Compatibilité avec les outils existants*** : PostgreSQL est compatible avec de nombreux outils et bibliothèques tiers, facilitant ainsi l'intégration de notre application avec d'autres services ou systèmes. Et bien que pour l'instant nous le déployons en local, cela nous permets de nous projeter dans un déploiement en serverless si besoin sans avoir à craindre d'important changement.
    3. ***Son niveau de sécurité : En effet, il dispose de mécanisme de sécurité robustes, comme la gestion des utilisateurs, les autorisations d'accès aux données ce qui ainsi à assurer une protection de nos données sensibles.

Cela dit, comme toutes technologies, il est important d'énoncer certaines limites que nous pourront avoir à faire face à l'avenir liés à ces choix : 

1. ***Temps de réponse*** : Même si PostgreSQL est une SGBD (Système de Gestion de Base de Données) robuste, il peut y avoir un certain délai d'accès aux données ce qui peut provoquer une certaine marge d'attente sur le temps de réponse. ce qui n'est pas l'idéal dans une app comme la notre qui se veut avoir un temps de réponse très rapide.
2. ***Coûts potentiels*** : Bien que PostgreSQL soit une base de données open source, si on décide de passer dans le cloud, des coûts peuvent lui être associés dû à la gestion de serveurs, de sauvegarde...etc.
3. ***Dépendance aux extensions*** : Pour ajouter des fonctionnalités à notre application, on devra souvent utiliser des extensions tierces. Cela nous expose à une forte dépendance de la qualité et compatibilité de ces extensions, ce qui entraine alors de potentiels risques.
4. Pour des applications telles que la notre dans l'état actuel, Flask semble être une très bonne solution, mais si on devrait revoir notre application de manière à ce qu'elle soit gourmandes en ressources où à très grandes échelles, il y a de forte chance que flash présente des limites de performances. Ainsi, il serait plus judicieux d'anticiper un changement de Framework en allant vers un autre Framework python plus complet tel que Django. 


## Structure Base de données
<img width="94" alt="image" src="https://github.com/Ben-Hadji/microservices/assets/83819844/5c619505-428d-4434-970a-900b0c6e9cec">


## Architecture

- your_project_folder/
  - app/
    - app.py
    - templates/
      - index.html
  - postgres/
    - init_db
    - dockerfile
  - dockercompose.yaml 
