class Livre:
	def __init__(self,titre="",année=None,genre=""):
		self.titre = titre
		self.année = année
		self.genre = genre
	
	
	def __str__(self):
		if self.genre == "": 
			return f"{self.année} {self.titre}"
		else:
			return f"{self.année} [{self.genre}] {self.titre}"
	
	
	def __lt__(self,autre_livre):
		# Compare les années des deux livres
		if self.année < autre_livre.année:
			return True
		# Si les années sont égales, compare les genres en utilisant l'ordre défini dans ordre_des_genres
		elif self.année == autre_livre.année:
			if self.genre < autre_livre.genre:
				return True
            # Si les genres sont égaux, compare les titres en utilisant l'ordre lexicographique
			elif self.genre == autre_livre.genre:
				return self.titre < autre_livre.titre
			return False
	
	
	#converstion en json
	def conv_json(self):
		return {
		"titre":self.titre,
		"annee":self.année,
		"genre":self.genre
		}
