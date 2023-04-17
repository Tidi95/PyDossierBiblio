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
