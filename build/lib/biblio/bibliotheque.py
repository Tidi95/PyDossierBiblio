class Bibliotheque:
	def __init__(self):
		self.livres=[]
		self.genres=[]
	def ajoute_genre(self,genre):
		self.genres.append(genre)
	def genre_existe(self,genre):
		return genre in self.genres
	def ajoute_livre(self,livre):
		self.livres.append(livre)
	#def ajoute_livre(self,livre):
	#	self.livre.append(livre)
	#def affiche_livre(self):
		#pass

