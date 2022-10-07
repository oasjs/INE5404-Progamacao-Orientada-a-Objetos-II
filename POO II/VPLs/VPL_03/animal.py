from abc import ABC, abstractmethod

class Animal(ABC):
	def __init__(self, tamanhoPasso: int):
		self.__tamanhoPasso = tamanhoPasso
	
	@property
	def tamanhoPasso(self):
		return self.__tamanhoPasso

	@tamanhoPasso.setter
	def tamanhoPasso(self, tamanhoPasso: int):
		self.__tamanhoPasso = tamanhoPasso

	@abstractmethod
	def mover(self):
		pass

	@abstractmethod
	def produzirSom(self):
		pass