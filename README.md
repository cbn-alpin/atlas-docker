# GeoNature Atlas Docker

Ce dépôt contient les fichiers nécessaires au test local des
images Docker de l'Atlas et de ses scripts d'installation.

L'Atlas fonctionne dans un container Docker et installe ses schémas dans une base GeoNature présente sur la machine hôte. Il n'utilise pas de FDW
pour les tables de GeoNature.

## Préparation
- Cloner ce dépôt sur votre machine.
- Créer un fichier `.env` à partir du fichier `.env.sample` avec : `cp .env.sample .env`
- Adapter les paramètres de votre fichier `.env` à votre installation.
- Créer un fichier `data/atlas/config/config.py` à partir du fichier `data/atlas/config/config.py` avec : `cp data/atlas/config/config.sample.py data/atlas/config/config.py`
- Paramètrer votre Atlas dans le fichier `data/atlas/config/config.py`
- Si nécessaire personnaliser votre Atlas (CSS, territoire, templates, images, ...) dans le dossier `data/atlas/custom/` (voir documentation de l'Atlas).

## Installation de la base de données
- Mettre à `true` les 2 variables `ATLAS_INSTALL_SCHEMA` et `ATLAS_RESET_SCHEMA` de votre fichier `.env`.
- Lancer l'insllation en démarrant le container : `docker compose up`
- Une fois l'installation terminé mettre `ATLAS_RESET_SCHEMA` à `false` dans le fichier `.env`.