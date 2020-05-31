# Mise en place de la base de données

# Import de la base de données
from .. app import db

# Création d'une classe par table et une ligne par colonne

# Table personne
class Personne(db.Model):
	pers_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
	pers_nom = db.Column(db.Text)
	pers_prenom = db.Column(db.Text)
	pers_autre_nom = db.Column(db.Text)
	pers_naissance = db.Column(db.Text)
	pers_mort = db.Column(db.Text)
	pers_titre = db.Column(db.Text)
	pers_fonction = db.Column(db.Text)
	pers_image = db.Column(db.Boolean)
	pers_url = db.Column(db.Text)
	pers_description = db.Column(db.Text)
	citeP = db.relationship('CiteP', back_populates='personne')

# Table lieu
class Lieu(db.Model):
	lieu_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
	lieu_nom = db.Column(db.Text)
	lieu_ville = db.Column(db.Text)
	lieu_dpt = db.Column(db.Text)
	lieu_latitude = db.Column(db.Float)
	lieu_longitude = db.Column(db.Float)
	lieu_url = db.Column(db.Text)
	lieu_description = db.Column(db.Text)
	citeL = db.relationship('CiteL', back_populates='lieu')
	
# Table lettre
class Lettre(db.Model):
	lettre_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
	lettre_date = db.Column(db.Text)
	lettre_lieu = db.Column(db.Text)
	lettre_expediteur = db.Column(db.Text)
	lettre_destinataire = db.Column(db.Text)
	citeP = db.relationship('CiteP', back_populates='lettre')
	citeL = db.relationship('CiteL', back_populates='lettre')

# Table citation (personnes)
class CiteP(db.Model):
	citeP_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
	citeP_lettre_id = db.Column(db.Integer, db.ForeignKey('lettre.lettre_id'))
	citeP_pers_id = db.Column(db.Integer, db.ForeignKey('personne.pers_id'))
	personne = db.relationship('Personne', back_populates='citeP')
	lettre = db.relationship('Lettre', back_populates='citeP')

# Table citation (lieux)
class CiteL(db.Model):
	citeL_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
	citeL_lettre_id = db.Column(db.Integer, db.ForeignKey('lettre.lettre_id'))
	citeL_lieu_id = db.Column(db.Integer, db.ForeignKey('lieu.lieu_id'))
	lieu = db.relationship('Lieu', back_populates='citeL')
	lettre = db.relationship('Lettre', back_populates='citeL')