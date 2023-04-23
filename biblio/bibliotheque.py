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
