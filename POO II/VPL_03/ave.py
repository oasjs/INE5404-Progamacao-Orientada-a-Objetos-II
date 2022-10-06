from abc import ABC, abstractmethod
from animal import Animal

class Ave(Animal, ABC):
    def __init__(self, tamanho_passo: int, altura_voo: int):
        super().__init__(tamanho_passo)
        self._altura_voo = altura_voo

    @property
    def altura_voo(self):
        return self._altura_voo

    @altura_voo.setter
    def altura_voo(self, altura_voo: int):
        self._altura_voo = altura_voo

    def mover(self):
        return f'ANIMAL: DESLOCOU {self.altura_voo} VOANDO'

    @abstractmethod
    def produzirSom(self):
        pass