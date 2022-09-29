from abc import ABC, abstractmethod

class Animal(ABC):
	def __init__(self, tamanhoPasso: int):
		self._tamanhoPasso = tamanhoPasso


	"""Insira aqui os outros metodos"""
	
	@abstractmethod
	def produzirSom(self):
		pass

	@abstractmethod
	def tamanhoPasso(self):
		pass

	@abstractmethod
	@tamanhoPasso.setter
	def tamanhoPasso(self, tamanhoPasso: int):
		pass
	
	@abstractmethod
	def mover(self):
		pass

	@abstractmethod
	def produzirSom(self):
		pass