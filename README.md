# Projet Django - Guide de Collaboration

Bienvenue dans ce projet Django ! Ce guide vous aidera à cloner, configurer et exécuter le projet sur votre machine locale.

---

# 📋 Prérequis

Avant de commencer, assurez-vous d'avoir les outils suivants installés sur votre machine :

- **Python 3.8+**  
  [Télécharger Python 3.13.0 (Windows)](https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe) + Ajoutez (`PATH`) à la variable d'environnement système.
- **Git**
- **pip** (inclus avec Python)
- **venv** (inclus avec Python)

# 🚀 Instructions pour démarrer
 ## Executer les commande dans le terminale de VScode:

## 1. Clone et entre dans le répertoire :
```bash
git clone <URL-du-dépôt>
cd <nom-du-projet>
```

## 2. Crée un environnement virtuel :
```bash
python -m venv venv
```

## 2. Activer l'environnement virtuel :
```bash
venv\Scripts\activate
```
## 4. Installer les dépendances du projet :
```bash
pip install -r requirements.txt
```
  #### Remarque: le fichier "requirements.txt" doit déjà exister dans le Repo
   ##### Sinon, demandez au propriétaire du dépôt d'éxecuter :


## 5. Appliquer les migrations :
```bash
python manage.py migrate
```

## 6. Run Server:
```bash
python manage.py runserver
```

