# Paramétrage de la classe User 

# Import de la base de données et de login pour gérer les utilisateurs
from .. app import db, login

# Import de generate_password_hash et check_password_hash depuis le package Werkzeug Security pour assurer la sécurité des mots de passe
from werkzeug.security import generate_password_hash, check_password_hash

# Import de UserMixin depuis le package flask_login qui fournit les méthodes nécessaires à la gestion des utilisateurs (is_authenticated, is_active, is_anonymous, get_id)
from flask_login import UserMixin

# Création de la table utilisateur et de ses colonnes
# Avec UserMixin, on signale à Python que la classe User n'est pas seulement une table dans une BD mais qu'elle correspond aussi à un modèle utilisateur nécessitant des méthodes particulières
class User(UserMixin, db.Model):
	user_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
	user_nom = db.Column(db.Text, nullable=False)
	user_login = db.Column(db.String(45), nullable=False, unique=True)
	user_email = db.Column(db.Text, nullable=False)
	user_password = db.Column(db.String(64), nullable=False)

	@staticmethod
	def identification(login, motdepasse):
		"""
		Fonction qui identifie un utilisateur. Si cela fonctionne, renvoie les données de l'utilisateurs
        :param login: identifiant de l'utilisateur
        :param motdepasse: mot de passe de l'utilisateur
        :returns: si réussite, données de l'utilisateur, sinon none
        :rtype: user ou none
		"""
		utilisateur = User.query.filter(User.user_login == login).first()
		if utilisateur and check_password_hash(utilisateur.user_password, motdepasse):
			return utilisateur
		return None

	@staticmethod
	def creer(login, email, nom, motdepasse):
		"""
		Fonction qui crée un compte utilisateur. Retourne un tuple (booléen, user ou liste)
        Si il y a une erreur, la fonction renvoie False suivi d'une liste d'erreur
        Sinon, elle renvoie True suivi de la donnée enregistrée

        :param login: login de l'utilisateur
        :param email: email de l'utilisateur
        :param nom: nom de l'utilisateur
        :param motdepasse: mot de passe de l'utilisateur (minimum 8 caractères)
        :returns: tuple
		"""
		erreurs = []
		# Vérification que tous les champs du formulaire sont complétés
		if not login:
			erreurs.append("Entrez un login")
		if not email:
			erreurs.append("Entrez une adresse mail")
		if not nom:
			erreurs.append("Entrez un nom")
		if not motdepasse or len(motdepasse) < 8:
			erreurs.append("Entrez un mot de passe valide (>8 caractères)")

        # Vérification que personne n'a utilisé cet email ou ce login
		uniques = User.query.filter(
			db.or_(User.user_email == email, User.user_login == login)
		).count()
		if uniques > 0:
			erreurs.append("L'adresse mail ou le login sont déjà utilisés")

        # Si il y a au moins une erreur
		if len(erreurs) > 0:
			return False, erreurs

        # Création d'un utilisateur
		utilisateur = User(
			user_nom=nom,
			user_login=login,
			user_email=email,
			user_password=generate_password_hash(motdepasse)
		)

		try:
			# Ajout du nouvel utilisateur au transport vers la base de données
			db.session.add(utilisateur)
			# Envoi du paquet
			db.session.commit()
			# Utilisateur envoyé en retour
			return True, utilisateur
		except Exception as erreur:
			return False, [str(erreur)]

	def get_id(self):
		"""
		Fonction qui retourne l'id de l'object actuellement utilisé
		:param self
		:returns: id de l'utilisateur
		:rtype: integer
		"""
		return(self.user_id)

@login.user_loader
def trouver_utilisateur_via_id(user_id):
	"""
	Fonction qui permet de récupérer un utilisateur selon son identifiant
	:param user_id: id de l'utilisateur
	:type user_id : integer
	:returns: id de l'utilisateur
	:rtype: integer
	"""
	return User.query.get(int(user_id))