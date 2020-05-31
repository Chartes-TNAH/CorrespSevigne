# Initialisation de l'app et de la base de données

# Import du module Flask depuis le package flask
from flask import Flask

# Import du module SQLAlchemy depuis le package flask_sqlalchemy pour faire fonctionner la base de données
from flask_sqlalchemy import SQLAlchemy
# Import du module LoginManager depuis le package flask_login pour gérer les utilisateurs
from flask_login import LoginManager

# Import du module os pour que Python s'adapte au système d'exploitation du PC
# Import du module os.path pour manipuler les chemins de fichiers et de répertoires
import os
import os.path

# Import de la variable SECRET_KEY depuis le fichier constantes
from .constantes import SECRET_KEY

# Définition des chemins
# Chemin du fichier courant
chemin_actuel = os.path.dirname(os.path.abspath(__file__))
# Chemin vers les templates
templates = os.path.join(chemin_actuel, "templates")
# Chemin vers les éléments "static"
statics = os.path.join(chemin_actuel, "static")

# Instanciation de l'app
# Précision du nom de l'app
# Définition des dossiers contenant les templates et les élements "static"
app = Flask("CorrespSevigne",
	template_folder=templates,
    static_folder=statics
	)

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./CorrespSevigne_BD.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialisation de l'objet db
db = SQLAlchemy(app)
# Initialisation de l'objet login (pour la gestion des utilisateurs)
login = LoginManager(app)

# Configuration de la clef secrète pour faire fonctionner les sessions
app.config['SECRET_KEY'] = SECRET_KEY

# Importation des routes pour les relier à l'app
from .routes import generic, error