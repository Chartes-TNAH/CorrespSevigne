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

## Lancement de l'application CorrespSevigne

Au préalable, installer Python3.
Puis : 
- Cloner le dépôt GIT: 'git clone https://github.com/MorganeRlt/CorrespSevigne.git'
- Entrer dans le dépôt
- Installer un environnement virtuel : 'virtualenv -p python3 env'
- Activer l'environnement virtuel : 'source env/bin/activate' (à répéter à chaque lancement de l'app)
- Installer les packages : 'pip install -r requirements.txt'
- Lancer l'app : 'python3 run.py'

## Crédits

Les portraits proviennent des bases de données Joconde et Paris Musées Collections.

Les lettres ont été encodées à partir de l'édition du corpus dirigée par Pierre-Marie Gault de Saint-Germain en 1823 chez Dalibon. L'édition a été numérisée et est disponible sur Gallica à cette adresse : https://gallica.bnf.fr/ark:/12148/bpt6k6323006w/f7.item.
