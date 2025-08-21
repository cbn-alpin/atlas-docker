# -*- coding:utf-8 -*-
# Fichier de configuration
# WARNING: don't write secret here, use environment variables in .env file..

# Nom de la structure
STRUCTURE = "CBNA"

# Nom de l'application
NOM_APPLICATION = "Atlas Docker - LOCAL"

# Enable organism module : organism sheet + organism participation on species sheet
ORGANISM_MODULE = False

# Recharger automatiquement les templates
TEMPLATES_AUTO_RELOAD = True

# +---------------------------------------------------------------------+
# Multilingual

# Default language, also used when multilingual is disabled
DEFAULT_LANGUAGE = 'fr'

# Activate multilingual
MULTILINGUAL = False

# Available languages
# Don't delete, even if you disable MULTILINGUAL
# You need to add your own default language (DEFAULT_LANGUAGE) here if it's not present
# Check documentation to add another language
LANGUAGES = {
    'en': {
        'name' : 'English',
        'flag_icon' : 'flag-icon-gb',
        'months' : ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        },
    'fr': {
        'name' : 'Français',
        'flag_icon' : 'flag-icon-fr',
        'months' : ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Decembre']
        },
    'it': {
        'name' : 'Italiano',
        'flag_icon' : 'flag-icon-it',
        'months' : ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre']
        }
}
# +---------------------------------------------------------------------+
# Cartographie

# Configuration des cartes (centre du territoire, couches CARTE et ORTHO, échelle par défaut...)
MAP = {
    'LAT_LONG': [44.7952, 6.2287],
    'FIRST_MAP': {
            'url' : '//{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
            'attribution' : '&copy OpenStreetMap',
            'tileName' : 'OSM'
    },
    'SECOND_MAP' : {'url' :'//a.tile.opentopomap.org/{z}/{x}/{y}.png',
            'attribution' : '&copy OpenStreetMap-contributors, SRTM | Style: &copy OpenTopoMap (CC-BY-SA)',
            'tileName' : 'OTM'
    },
    'ZOOM' : 10,
    # Pas du slider sur les annees d'observations: 1 = pas de 1 an sur le slider
    'STEP': 1,
    # Couleur et épaisseur des limites du territoire
    'BORDERS_COLOR': '#000000',
    'BORDERS_WEIGHT': 3,
    'ENABLE_SLIDER': True
}

# -------------------------------------------------------------------------------
# Fiche espèce

# Rang taxonomique qui fixe jusqu'à quel taxon remonte la filiation taxonomique (hierarchie dans la fiche d'identite : Famille, Ordre etc... )
LIMIT_RANG_TAXONOMIQUE_HIERARCHIE = 13

# Rang taxonomique qui fixe la limite de l'affichage de la fiche espece ou de la liste
# 35 = ESPECE
# On prend alors tout ce qui est inferieur ou egal a l'espece pour faire des fiches et ce qui est superieur pour les listes
LIMIT_FICHE_LISTE_HIERARCHY = 35

# Coupe le nom_vernaculaire à la 1ere virgule sur les fiches espèces
SPLIT_NOM_VERN = True

#### ID DES ATTRIBUTS DESCRIPTIFS DES TAXONS DE LA TABLE vm_taxon_attribute
TAXHUB_DISPLAYED_ATTR = ["sinp_description", "sinp_ecology", "sinp_uses"]
