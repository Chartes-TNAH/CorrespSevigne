# Définition d'une variable fixe qui permet de sécuriser les transactions en stockant une clef secrète régénérée à chaque initialisation de l'app

from warnings import warn

SECRET_KEY = "JE SUIS UN SECRET !"

if SECRET_KEY == "JE SUIS UN SECRET !":
    warn("Le secret par défaut n'a pas été changé, vous devriez le faire", Warning)