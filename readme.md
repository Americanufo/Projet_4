# Chess Manager

Chess Manager est une application Python permettant de gérer des joueurs, des tournois d’échecs, la saisie des scores, la reprise de tournoi, et la génération de rapports.

## Prérequis

- Python 3.12.7 ou supérieur
- Utiliser environnement virtuel (recommandé)
- Les dépendances du projet (voir ci-dessous)

## Installation

1. **Clonez le dépôt ou téléchargez les fichiers du projet.**
2. **Créez et activez un environnement virtuel :**
    ```
    python3 -m venv env
    source env/bin/activate  
    # Sur Windows : env\Scripts\activate
    ```
3. **Installez les dépendances :**
    ```
    pip install -r requirements.txt
    ```

## Lancer le programme

Dans le terminal, à la racine du projet :
python3 main.py

Vous verrez le menu principal s’afficher dans le terminal.

## Utilisation

- **Ajouter un joueur :** Suivez les instructions du menu pour saisir les informations du joueur.
- **Créer un tournoi :** Saisissez les informations demandées (nom, lieu, dates, joueurs, etc.).
- **Reprise d’un tournoi en cours :** Sélectionnez un tournoi non terminé pour le reprendre là où il s’était arrêté.
- **Voir les rapports :** Accédez à l’historique des tournois, classements et détails des matchs.

## Générer un rapport Flake8 HTML

Pour vérifier la qualité du code et générer un rapport HTML :

1. **Activez votre environnement virtuel si ce n’est pas déjà fait :**
    ```
    source env/bin/activate
    ```

2. **Assurez-vous d’utiliser Flake8 version 6.x (et non 7.x) :**
    ```
    python -m flake8 --version
    ```

3. **Générez le rapport HTML Flake8 tout en ignorant les dossiers concernant l'environnement virtuel:**
    ```
    python -m flake8 --exclude=env,venv,.venv,flake-report,__pycache__ --format=html --htmldir=flake-report
    ```

4. **Ouvrez le rapport dans votre navigateur :**
    - Fichier principal : `flake-report/index.html`
    - Vérifiez qu’il n’y a **aucune erreur** listée dans le rapport.

## Structure du livrable

- `main.py`, `controllers/`, `models/`, `views/`, etc. : code source du projet
- `flake-report/` : le dossier contenant le rapport HTML généré par Flake8


## Conseils

- En cas d’erreurs Flake8, ouvrez le rapport HTML, corrigez les fichiers concernés, puis regénérez le rapport jusqu’à obtenir 0 erreur.
- Utilisez un éditeur comme VS Code avec l’extension Python et Flake8 activée pour corriger les erreurs en direct.

