from abc import ABC, abstractmethod
from animal import Animal

class Mamifero(Animal, ABC): 
    def __init__(self, volume_som: int, tamanho_passo: int):
        super().__init__(tamanho_passo)
        self._volumeSom = volume_som

    @property
    def volumeSom(self):
        return self._volumeSom

    @volumeSom.setter
    def volumeSom(self, volume_som: int):
        self._volumeSom = volume_som

    @abstractmethod
    def produzirSom(self, volumeSom):
        pass
