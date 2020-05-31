# Gestion des erreurs

# render_template relie les templates aux routes
from flask import render_template
# import de l'application
from ..app import app

# Page introuvable
# Le décorateur errorhandler() enregistre une fonction avec un code erreur pour pouvoir retourner une page d'erreur en fonction de la réponse HTTP
@app.errorhandler(404)
def not_found(erreur):

	"""
	Fonction servant à renvoyer vers la page prévue en cas d'erreur (ici 404)
	:param erreur
	:returns: template
	:rtype: fichier HTML
	"""

	return render_template("pages/erreurs/404.html"), 404

# Erreur interne du serveur
@app.errorhandler(500)
def internal_error(erreur):
	return render_template("pages/erreurs/500.html"), 500

# Accès non autorisé
@app.errorhandler(401)
def not_authorized(erreur):
	return render_template("pages/erreurs/401.html"), 401