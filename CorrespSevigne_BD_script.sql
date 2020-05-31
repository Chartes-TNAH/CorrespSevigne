PRAGMA encoding = 'UTF-8';

-- Création de la table user :
CREATE TABLE user (
  user_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT,
  user_nom TINYTEXT NOT NULL,
  user_login VARCHAR(45) NOT NULL,
  user_email TINYTEXT NOT NULL,
  user_password VARCHAR(100) NOT NULL
);

-- Création de la table lieu :
CREATE TABLE lieu (
  lieu_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  lieu_nom TEXT NOT NULL,
  lieu_ville TEXT,
  lieu_dpt TEXT,
  lieu_latitude NUMERIC,
  lieu_longitude NUMERIC,
  lieu_url TEXT NULL,
  lieu_description TEXT
);

-- Création de la table lettre :
CREATE TABLE lettre (
  lettre_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT,
  lettre_date TEXT,
  lettre_lieu TEXT,
  lettre_expediteur TEXT,
  lettre_destinataire TEXT
);

-- Création de la table personne :
CREATE TABLE personne (
  pers_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  pers_nom TEXT NOT NULL,
  pers_prenom TEXT,
  pers_autre_nom TEXT NULL,
  pers_naissance TEXT NULL,
  pers_mort TEXT NULL,
  pers_titre TEXT,
  pers_fonction TEXT,
  pers_image BOOLEAN DEFAULT NULL,
  pers_url TEXT NULL,
  pers_description TEXT
);

-- Création de la table citation des lieux :
CREATE TABLE citeL (
	citeL_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    citeL_lettre_id INTEGER NOT NULL,
    citeL_pers_id INTEGER NOT NULL
);

-- Création de la table citation des personnes :
CREATE TABLE citeP (
	citeP_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    citeP_lettre_id INTEGER NOT NULL,
    citeP_pers_id INTEGER NOT NULL
);

