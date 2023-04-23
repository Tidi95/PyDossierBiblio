#Commandes.py

def affiche_menu():
	print("""Menu principal
		   [M]   Menu principal
		   [LG]  Liste des Genres
		   [LL]  Liste des Livres
		   [NG]  Nouveau Genre
		   [NL]  Nouveau Livre
		   [SG]  Suppression d’un Genre
		   [SL]  Suppression d ’un Livre
		   [Q]   Quitter le programme
""")


def nouveau_genre(bibli):
	genre = input("Entrez le nom du genre : ").upper()
	if bibli.genre_existe(genre):
		print(f"\033[31mLe genre {genre} existe déjà dans la bibliotheque\033[0m")
	else:
		bibli.ajoute_genre(genre)
		print(f"Le genre {genre} a été créé")


def sauvegarde(texte_json,package_json):
    # Nom du fichier où les données seront sauvegardées
    nom_fichier = ".biblio.json"

    try:
        # Vérifie si le fichier existe et s'il est non vide
        with open(nom_fichier, "r") as f:
            contenu = package_json.load(f)
    except (FileNotFoundError, package_json.JSONDecodeError):
        # Si le fichier n'existe pas ou est vide, créez une liste vide
        contenu = []

    # Ajoutez les nouvelles données à la liste
    contenu.append(texte_json)

    # Sauvegardez la liste mise à jour dans le fichier JSON
    with open(nom_fichier, "w") as f:
        package_json.dump(contenu, f)


def nouveau_livre(bibli,livre,package_json):
	nom_livre = input("Entrez le nom du livre : ").upper()
	année_livre = input("Entrez l'année de parution du livre : ")
	#Verifions que c'est un int
	while not année_livre.isdigit():
		print("\033[31mLErreur : Veuillez entrer un entier.\033[0m")
		année_livre = input("Entrez l'année de parution du livre en entier (exemple: 2000): ")
	année_livre = int(année_livre)

	#Assurons nous que le genre existe dans notre biblio
	while True:
		genre_livre = input("Entrez le genre du livre : ").upper()
		if genre_livre == "":
			# Créez une nouvelle instance de la classe Livre en utilisant .__class__
			# Cela permet de créer un nouvel objet Livre sans importer la classe Livre dans ce fichier
			nouveau_livre = livre.__class__(nom_livre,année_livre,"")
			bibli.ajoute_livre(nouveau_livre)
			# Trie la liste de livres en utilisant la méthode __lt__ définie dans la classe Livre
			bibli.livres.sort()
			print(f"""Le livre "{nom_livre}" sans genre a été créé.""")
			#Enregistrement en json
			texte_json=nouveau_livre.conv_json()
			sauvegarde(texte_json,package_json)
			break
		else:
			if not bibli.genre_existe(genre_livre):
				print(f"""\033[31mLe genre {genre_livre} n'existe pas dans la bibliotheque 
créé la d'abord\033[0m""")
				break
			else:
				# Créez une nouvelle instance de la classe Livre en utilisant .__class__
				# Cela permet de créer un nouvel objet Livre sans importer la classe Livre dans ce fichier
				nouveau_livre = livre.__class__(nom_livre,année_livre,genre_livre)
				bibli.ajoute_livre(nouveau_livre)
				# Trie la liste de livres en utilisant la méthode __lt__ définie dans la classe Livre
				bibli.livres.sort()
				print(f"""Le livre "{nom_livre}" a été créé.""")
				#Enregistrement en json
				texte_json=nouveau_livre.conv_json()
				sauvegarde(texte_json,package_json)
				return False


def recharge(fichier_json,bibli,livre_cls,package_json):
	# Chargez les données depuis le fichier JSON
	with open(fichier_json, "r") as f:
		file_content = f.read()
        # Vérifiez si le fichier est vide avant de charger les données en JSON
		if not file_content:
			print("Aucun livre n'est disponible dans la bibliothèque.")
			return
		data = package_json.loads(file_content)
	# Convertissez les dictionnaires en instances de Livre et ajoutez-les à la bibliothèque
	for livre_dict in data:
		livre = livre_cls(livre_dict["titre"], livre_dict["annee"], livre_dict["genre"])
		bibli.livres.append(livre)


def liste_livre(bibli,livre_cls,package_json):
	#fichier_json=".biblio.json"

	#recharge(fichier_json,bibli,livre_cls,package_json)
	for l in bibli.livres:
		print(l) # La méthode __str__() de la classe Livre est automatiquement appelée


#Trouvons le nombre de fois où mot se trouve dans liste
def occurence(liste,mot):
	occu = 0
	for i in liste: # dans notre cas i sera un objet de livre et on veux l'attribut genre
		if mot in i.genre:
			occu += 1
	return occu


def liste_genre(bibli):
	liv = bibli.livres
	gen = bibli.genres
	#Le genre des livres seront sauvegarder sans supprimer les livres
	for j in liv:
		if j.genre not in gen and j.genre != "":
			gen.append(j.genre)
	if len(bibli.genres) == 0:
		print("Aucun genre n'est disponible dans la bibliothèque.")
	for g in bibli.genres:
		n = occurence(bibli.livres,g)
		print(f"{g}: {n} livre(s)")


def sup_livre(bibli,package_json):
	nom_livre = input("Entrez le nom du livre : ").upper()
	année_livre = input("Entrez l'année de parution du livre : ")
	#Verifions que c'est un int
	while not année_livre.isdigit():
		print("\033[31mLErreur : Veuillez entrer un entier.\033[0m")
		année_livre = input("Entrez l'année de parution du livre en entier (exemple: 2000): ")
	année_livre = int(année_livre)
	nom_genre = input("Entrez le genre du livre : ").upper()
	n = 0
	liv = bibli.livres
	# J'ameliore la précision du supprime en regardant le nom la datte 
	# et le genre puis faison une mise à jour du fichier json en mm temps
	nom_fichier = ".biblio.json"
	for i in liv:
		if nom_livre == i.titre:
			if année_livre == i.année:
				if nom_genre == i.genre:
					liv.remove(i)
					n += 1
					contenu=[]
					# mise à jour de la liste dans le fichier JSON
					for j in liv:
						contenu.append(j.conv_json())
						with open(nom_fichier, "w") as f:
							package_json.dump(contenu, f)
	if n==0:
		print("Ce livre n’existe pas!")


def sup_genre(bibli,package_json):
	nom_genre = input("Entrez le nom du genre : ").upper()
	n = 0
	gen = bibli.genres
	liv = bibli.livres
	nom_fichier = ".biblio.json"
	for i in gen:
		if i == nom_genre:
			gen.remove(i)
			#Supprimons le genre des livres correspondants sans supprimer les livres
			for j in liv:
				if nom_genre == j.genre:
					j.genre = ""
			n += 1
			# mise à jour de la liste dans le fichier JSON
			contenu=[]
			for j in liv:
				contenu.append(j.conv_json())
				with open(nom_fichier, "w") as f:
					package_json.dump(contenu, f)
	if n==0:
		print("Ce genre n’existe pas!")
