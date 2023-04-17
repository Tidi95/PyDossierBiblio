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

def nouveau_livre(bibli,livre):
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
			#livre = {"nom": nom_livre, "année": année_livre, "genre": genre_livre}
			#bibli.ajoute_livre(livre)
			print(f"""Le livre "{nom_livre}" sans genre a été créé.""")
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
				# Créer un dictionnaire avec les informations saisies
				#livre = {"nom": nom_livre, "année": année_livre, "genre": genre_livre} 
				# Ajouter le dictionnaire à la liste des livres
				#bibli.ajoute_livre(livre)
				print(f"""Le livre "{nom_livre}" a été créé.""")
				return False
def liste_livre(bibli):
	if len(bibli.livres) == 0:
		print("Aucun livre n'est disponible dans la bibliothèque.")
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
	if len(bibli.genres) == 0:
		print("Aucun genre n'est disponible dans la bibliothèque.")
	for g in bibli.genres:
		n = occurence(bibli.livres,g)
		print(f"{g}: {n} livre(s)")
def sup_livre(bibli):
	nom_livre = input("Entrez le nom du livre : ").upper()
	n = 0
	liv = bibli.livres
	for i in liv:
		if nom_livre in i.titre:
			liv.remove(i)
			n += 1
	if n==0:
		print("Ce livre n’existe pas!")
def sup_genre(bibli):
	nom_genre = input("Entrez le nom du genre : ").upper()
	n = 0
	gen = bibli.genres
	for i in gen:
		if i == nom_genre:
			liv.remove(i)
			n += 1
	if n==0:
		print("Ce genre n’existe pas!")
