# CorrespSevigne

## Projet

"CorrespSevigne" est une application web créée en mai 2020 par Morgane Rousselot dans le cadre du Master 2 Technologies numériques appliquées à l'histoire de l'Ecole Nationale des Chartes (Paris).

Cette application propose une édition numérique de lettres de la marquise de Sévigné et de ses proches. L'accent est mis sur le réseau de sociabilité de la marquise et de sa famille.

Les fonctionnalités suivantes sont proposées : 
* consulter chaque lettre via un index ;
* consulter deux types de visualisation des données : une galerie et une carte ;
* effectuer une recherche parmi les personnes et les lieux cités dans les lettres.
Une inscription/connexion est nécessaire pour avoir accès à toutes les fonctionnalités.

L'application a été développée avec le langage de programmation Python 3 et le framework Flask. Le framework Bootstrap a été utilisé pour le graphisme.
Elle s'appuie sur deux types de données : 
- les lettres encodées en XML-TEI ;
- une base de données MySQL créée avec DB Browser qui contient les données concernant les personnes et les lieux cités dans les lettres.

## Arborescence de l'application CorrespSevigne

doc
app

---modeles
-----------__init__.py
-----------donnees.py
-----------utilisateurs.py

---routes
-----------error.py
-----------generic.py

---static
-----------css
-----------img
-----------js
-----------lettres

---templates
-----------pages
---------------------------erreurs
-------------------------------------------401.html
-------------------------------------------404.html
-------------------------------------------500.html
---------------------------accueil.html
---------------------------carte.html
---------------------------cite.html
---------------------------connexion.html
---------------------------galerie.html
---------------------------index.html
---------------------------inscription.html
---------------------------lettre.html
---------------------------lieu.html
---------------------------personne.html
---------------------------resultat.html
-----------partials
---------------------------footer.html
---------------------------forme.html
---------------------------metadata.html
-----------conteneur.html

---__init__.py
---app.py
---constantes.py

## Lancement de l'application CorrespSevigne

Installer Python3
1- Cloner le dépôt GIT: 'git clone https://github.com/MorganeRousselot/CorrespSevigne.git'
2- Entrer dans le dépôt
3- Installer un environnement virtuel : 'virtualenv -p python3 env'
4- Activer l'environnement virtuel : 'source env/bin/activate' (à répéter à chaque lancement de l'app)
5- Installer les packages : 'pip install -r requirements.txt'
6- Lancer l'app : 'python3 run.py'

## Crédits

Les portraits proviennent des bases de données Joconde et Paris Musées Collections.

Les lettres ont été encodées à partir de l'édition du corpus dirigée par Pierre-Marie Gault de Saint-Germain en 1823 chez Dalibon. L'édition a été numérisée et est disponible sur Gallica à cette adresse : https://gallica.bnf.fr/ark:/12148/bpt6k6323006w/f7.item.