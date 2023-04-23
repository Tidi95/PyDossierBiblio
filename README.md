# PyDossierBiblio

Ce projet est un paquet Python qui permet de gérer une bibliothèque de livres. Il comprend un programme principal qui permet de manipuler la bibliothèque.
Structure du répertoire

La structure du répertoire de notre projet est la suivante :

![image](https://user-images.githubusercontent.com/114936529/233851380-f4e3027b-9b0d-4e68-abb5-c5d3fd038121.png)

# Installation

Pour installer le paquet, exécutez la commande suivante :

### $ python setup.py install --user


L’option --user permet d’installer le paquet dans votre répertoire personnel. Si l’installation se passe bien, le script bibliodb sera présent dans le répertoire ~/.local/bin/. Si ce répertoire est dans votre variable d’environnement PATH, vous pouvez maintenant exécuter le script depuis n’importe quel répertoire sans préciser le chemin complet.
# Utilisation

Une fois installé, vous pouvez exécuter le programme principal bibliodb pour manipuler la bibliothèque. Lorsque vous lancez le programme, vous pouvez entrer les commandes suivantes :

    M pour afficher le menu des commandes
    LG pour afficher la liste des genres
    LL pour afficher la liste des livres
    NG pour ajouter un nouveau genre
    NL pour ajouter un nouveau livre
    SG pour supprimer un genre
    SL pour supprimer un livre
    Q pour quitter le programme

# Remarques

    Ajoutez des docstrings à vos fonctions, méthodes et modules.
    Commentez votre code.
    Respectez les règles de programmation : lignes de 80 caractères maximum, fonctions et méthodes de 30 lignes maximum.
    Ce projet est conçu pour fonctionner avec Python 3.
