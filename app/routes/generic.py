# Définition des routes générales

# Import de différentes variables depuis le package flask : 
# render_template relie les templates et les routes ;
# request récupère les infos d'un formulaire ;
# redirect redirige vers l'URL d'une autre route ;
# flash envoie des messages flash ;
# url_for permet de construire des URLs vers les fonctions et les pages HTML
from flask import render_template, request, redirect, flash, url_for

# Import de différentes variables depuis le package flask_login pour gérer les connexions (authentification, récupération de l'utilisateur courant, déconnexion, limitation de l'accès à des pages)
from flask_login import login_user, current_user, logout_user, login_required

# Import du module SQLAlchemy depuis le package flask_sqlalchemy pour faire fonctionner la base de données
from flask_sqlalchemy import SQLAlchemy
# Import de l'opérateur de filtre or_ depuis le package sqlalchemy
from sqlalchemy import or_

# Import du package lxml pour afficher le contenu d'un doc XML dans l'app
from lxml import etree

# Importation des objets des fichiers .py app, données et utilisateurs
from ..app import app, db, login
from ..modeles.donnees import Personne, Lieu, Lettre, CiteP, CiteL
from ..modeles.utilisateurs import User

# Définition du nombre de résultats acceptés par page dans le cadre d'une recherche
RESULTATS_PAR_PAGE = 5

# Définition des routes

# Route vers l'accueil
# Le décorateur associe l'URL (entre parenthèses) et la fonction qui suit
@app.route("/")
def accueil():
    """
    Fonction permettant l'affichage de la page d'accueil
    :returns: template de l'accueil
    :rtype: page HTML
    """
    lettres = Lettre.query.order_by(Lettre.lettre_id).all()
    # La fonction render_template prend ici deux arguments : en premier le chemin vers le template, en deuxième un un argument nommé utilisé comme une variable dans le template
    return render_template("pages/accueil.html", lettres=lettres)

# Route vers la galerie des portraits
@app.route("/galerie")
#
@login_required
def galerie():
    """
    Fonction permettant l'affichage de la page de la galerie
    :returns: template de la galerie
    :rtype: page HTML
    """
    portraits = Personne.query.order_by(Personne.pers_image.desc()).all()
    return render_template("pages/galerie.html", personnes=portraits)

# Route vers la carte
@app.route("/carte")
@login_required
def carte():
    """
    Fonction permettant l'affichage de la page de la carte
    :returns: template de la carte
    :rtype: page HTML
    """
    lieux = Lieu.query.all()
    return render_template("pages/carte.html", carte=lieux)

# Route vers l'index des lettres
@app.route("/index")
def index():
    """
    Fonction permettant l'affichage de la page de l'index   
    :returns: template de l'index
    :rtype: page HTML
    """
    lettres = Lettre.query.order_by(Lettre.lettre_id).all()
    return render_template("pages/index.html", lettres=lettres)

# Route vers les lettres
@app.route("/lettre/<int:numero>")
@login_required
def lettre(numero):
    """
    Fonction permettant l'affichage de la page de chaque lettre en fonction du paramètre donné dans la variable définie dans le fichier XSLT   
    :param numero: variable définie dans le fichier XSLT pour distinguer chaque lettre
    :type numero: integer puis string
    :returns: template des lettres
    :rtype: page HTML
    """
    # Parsage du doc XML et stockage de ce parsage dans la variable source_doc
    source_doc = etree.parse("app/static/lettres/lettres.xml")
    # Parsage du doc XSLT et stockage de ce parsage dans la variable xslt_doc
    xslt_doc = etree.parse("app/static/lettres/lettres.xslt")
    # On indique à lxml que xslt_doc est bien une feuille de transformation XSL et on stocke le résultat dans la variable xslt_transformer
    xslt_transformer = etree.XSLT(xslt_doc) 
    # Stockage du résultat de la transformation XSLT
    output_doc = xslt_transformer(source_doc, numero=str(numero))
    return render_template("pages/lettre.html", HTML=output_doc, numero=numero)

# Route vers les lettres
@app.route("/cite/<int:numero>/<int:ref>")
@login_required
def cite(numero, ref):
    """
    Fonction permettant l'affichage de la page de chaque lettre reliée aux notices des personnes selon le paramètre donné dans le fichier XSLT
    :param numero, ref: variables définies dans le fichier XSLT pour distinguer chaque lettre
    :type numero, ref: integer puis string
    :returns: template des lettres
    :rtype: page HTML
    """
    # Parsage du doc XML et stockage de ce parsage dans la variable source_doc
    source_doc = etree.parse("app/static/lettres/lettres.xml")
    # Parsage du doc XSLT et stockage de ce parsage dans la variable xslt_doc
    xslt_doc = etree.parse("app/static/lettres/cite.xslt")
    # On indique à lxml que xslt_doc est bien une feuille de transformation XSL et on stocke le résultat dans la variable xslt_transformer
    xslt_transformer = etree.XSLT(xslt_doc) 
    # Stockage du résultat de la transformation XSLT
    output_doc = xslt_transformer(source_doc, numero=str(numero), ref=str(ref))
    return render_template("pages/cite.html", HTML=output_doc, numero=numero, ref=ref)

# Route vers les notices des personnes
@app.route("/personne/<int:pers_id>")
@login_required
def personne(pers_id):
    """
    Fonction permettant l'affichage de la page de chaque personne
    :param pers_id: id de chaque personne
    :type pers_id: integer
    :returns: template de chaque personne
    :rtype: page HTML
    """
    unique_personne = Personne.query.get_or_404(pers_id)
    citeP = CiteP.query.filter(CiteP.citeP_pers_id == Personne.pers_id)
    source = Lettre.query.filter(Lettre.lettre_id == CiteP.citeP_lettre_id)
    return render_template("pages/personne.html", personne=unique_personne, cite=citeP, source=source)

# Route vers les notices des lieux
@app.route("/lieu/<int:lieu_id>")
@login_required
def lieu(lieu_id):
    """
    Fonction permettant l'affichage de la page de chaque lieu    
    :param lieu_id: id de chaque lieu
    :type lieu_id: integer
    :returns: template de chaque lieu
    :rtype: page HTML
    """
    unique_lieu = Lieu.query.get_or_404(lieu_id)
    citeL = CiteL.query.filter(CiteL.citeL_lieu_id == Lieu.lieu_id)
    source = Lettre.query.filter(Lettre.lettre_id == CiteL.citeL_lettre_id)
    return render_template("pages/lieu.html", lieu=unique_lieu, cite=citeL, source=source)

# Route vers les résultats
@app.route("/resultat")
@login_required
def resultat():
    """
    Fonction permettant la recherche plein-texte et l'affichage de la page des résultats 
    :returns: template des résultats
    :rtype: page HTML
    """

    # On préfèrera l'utilisation de .get() ici
    #   qui nous permet d'éviter un if long (if "clef" in dictionnaire and dictonnaire["clef"])

    # Stockage dans une variable motclef des mot-clefs rentrés par l'utilisateur
    motclef = request.args.get("keyword", None)
    
    # Stockage dans une variable page d'un numéro de page
    page = request.args.get("page", 1)
    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1

    # Création d'une liste de vide de résultats pour chaque type de données recherchées
    resultats_lieu = []
    resultats_personne = []

    titre = "Resultat"

    # Si un mot-clef est rentré par l'utilisateur
    if motclef:
        # alors on stocke dans chaque liste vide de résultats créée plus haut le résultat de la requête effectuée dans chaque table 
        # de la base de données pour vérifier la concordance entre le mot-clef donné et les données stockées dans la BD
        # les résultats sont ensuite ordonnés selon un ordre ascendant et une pagination est créée
        resultats_personne = Personne.query.filter(
        	or_(
            	Personne.pers_nom.like("%{}%".format(motclef)),
            	Personne.pers_prenom.like("%{}%".format(motclef)),
        		Personne.pers_autre_nom.like("%{}%".format(motclef)),
        		Personne.pers_naissance.like("%{}%".format(motclef)),
        		Personne.pers_mort.like("%{}%".format(motclef)),
        		Personne.pers_titre.like("%{}%".format(motclef)),
        		Personne.pers_fonction.like("%{}%".format(motclef)),
        		)
        ).order_by(Personne.pers_nom.asc()).paginate(page=page, per_page=RESULTATS_PAR_PAGE)
        
        resultats_lieu = Lieu.query.filter(
            or_(
                Lieu.lieu_nom.like("%{}%".format(motclef)),
                Lieu.lieu_ville.like("%{}%".format(motclef)),
                Lieu.lieu_dpt.like("%{}%".format(motclef)),
                )
        ).order_by(Lieu.lieu_nom.asc()).paginate(page=page, per_page=RESULTATS_PAR_PAGE)
        
        titre = "Résultat pour la recherche `" + motclef + "`"

    return render_template(
        "pages/resultat.html",
        resultats_personne=resultats_personne,
        resultats_lieu=resultats_lieu,
        titre=titre,
        keyword=motclef)

# Route vers le formulaire d'inscription
@app.route("/register", methods=["GET", "POST"])
def inscription():
    """
    Fonction gérant les inscriptions et permettant l'affichage de la page d'inscription   
    :returns: template d'inscription ou d'accueil
    :rtype: page HTML
    """
    if request.method == "POST":
        statut, donnees = User.creer(
            login=request.form.get("login", None),
            email=request.form.get("email", None),
            nom=request.form.get("nom", None),
            motdepasse=request.form.get("motdepasse", None)
        )
        if statut is True:
            flash("Enregistrement effectué. Identifiez-vous maintenant", "success")
            return redirect("/")
        else:
            flash("Les erreurs suivantes ont été rencontrées : " + ",".join(donnees), "error")
            return render_template("pages/inscription.html")
    else:
        return render_template("pages/inscription.html")

# Route vers le formulaire de connexion
@app.route("/connexion", methods=["POST", "GET"])
def connexion():
    """
    Fonction gérant les connexions et permettant l'affichage de la page de connexion ou de celle de l'accueil
    :returns: template de connexion ou d'accueil
    :rtype: page HTML
    """
    # Si l'utilisateur est déjà connecté, il est redirigé vers la page d'accueil
    if current_user.is_authenticated is True:
        flash("Vous êtes déjà connecté.e", "info")
        return redirect("/")
    
    # Si l'utilisateur n'est pas connecté, on lui demande son login et son mot de passe (si l'un des deux manque, on lui indique une erreur)
    if request.method == "POST":
        utilisateur = User.identification(
            login=request.form.get("login", None),
            motdepasse=request.form.get("motdepasse", None)
        )
        if utilisateur:
            flash("Vous êtes connecté.e", "success")
            login_user(utilisateur)
            return redirect("/")
        else:
            flash("L'identifiant ou le mot de passe n'a pas été reconnu", "error")
    return render_template("pages/connexion.html")
login.login_view = 'connexion'

# Route pour se déconnecter (retour à la page d'accueil)
@app.route("/deconnexion", methods=["POST", "GET"])
def deconnexion():
    """
    Fonction gérant les déconnexions et permettant l'affichage de la page d'accueil    
    :returns: template d'accueil
    :rtype: page HTML
    """
    if current_user.is_authenticated is True:
        logout_user()
    flash("Vous êtes déconnecté.e", "info")
    return redirect("/")