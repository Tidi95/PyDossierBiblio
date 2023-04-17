#!/usr/bin/env python3
from setuptools import setup
import biblio
setup (
	name = "biblio" ,
	version = biblio.version,
	description ="un paquet pour gérer des bibliothèques" ,
	packages =["biblio"], # répertoire dans lequel se trouve le paquet
	scripts=["bibliodb"] # script contenu dans le paquet
)
