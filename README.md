## Books Online (fr)

bo_scraper est un outil permettant d'extraire des données du site [Book to Scrape](http://books.toscrape.com/).

Ce travail est issu du projet 2 de la formation DA Python OpenClassrooms.

Il est développé avec [Python 3.9.6](https://www.python.org/downloads/release/python-396/) sur Windows 10 Pro.

### Installer et éxécuter le programme

#### Cloner le projet, installer l'environnement virtuel et l'activer :

Rendez vous dans le dossier de votre choix et cloner le projet avec : \
`git clone https://github.com/Roxhe/bo-scraper.git`

Dans le dossier du projet, installer l'environnement virtuel avec : \
`python -m venv 'env'`

Puis activer le avec : \
`source env/scripts/activate`

#### Installer les modules nécessaire dans l'environnement virtuel :

Toujours dans le dossier du projet, exécuter : \
`pip install -r requirements.txt`

#### Executer le programme :

Dans le dossier du projet avec git et la commande : \
`python main.py`

Ou manuellement en double cliquant sur `main.py` dans le dossier du projet !

#### Résultat :

Le code va s'éxécuter pendant quelques minutes, il va récupérer différentes données pour chaques livres, créer un fichier csv par catégorie de livre, un fichier csv avec les données de tous les livres, un fichier csv avec les urls des couvertures de chaques livres, et un dossier `images` avec les couvertures de tous les livres en format jpg.

---


## Books Online (en)

bo_scraper is a tool for extracting data from the website [Book to Scrape](http://books.toscrape.com/)
This work come from the project 2 of the DA Python formation OpenClassrooms.

It will retrieve different data for each book and create a csv file per book category, a csv file with the data of all books, a csv file with the URLs of the covers of each book and an image folder with the covers of all books in jpg format.

It is developed with [Python 3.9.6](https://www.python.org/downloads/release/python-396/) on Windows 10 Pro.

### Install and run the program
