from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):
    
    def __init__(self, totalAndaresPredio: int, andarAtual, capacidade: int, totalPessoas: int):
        self._totalAndaresPredio = totalAndaresPredio
        self._andarAtual = andarAtual
        self._capacidade = capacidade
        self._totalPessoas = totalPessoas

    # ElevadorJahNoTerreoException
    def descer(self) -> str:
        if self._andarAtual > 0:
            self._andarAtual -= 1
            return "O elevador desceu 1 andar."
        else:
            raise ElevadorJahNoTerreoException
    
    # ElevadorCheioException
    def entraPessoa(self) -> str:
        if self._totalPessoas < self._capacidade:
            self._totalPessoas += 1
            return "Uma pessoa entrou no elevador."
        else:
            raise ElevadorCheioException
    
    # ElevadorJahVazioException
    def saiPessoa(self) -> str:
        if self._totalPessoas > 0:
            self._totalPessoas -= 1
            return "Uma pessoa saiu do elevador."
        else:
            raise ElevadorJahVazioException
    
    # ElevadorJahNoUltimoAndarException
    def subir(self) -> str:
        if self._andarAtual < self._totalAndaresPredio:
            self._andarAtual += 1
            return "O elevador subiu 1 andar."
        else:
            raise ElevadorJahNoUltimoAndarException
    
    @property
    def capacidade(self) -> int:
        return self._capacidade
    
    @property
    def totalPessoas(self) -> int:
        return self._totalPessoas
    
    @property    
    def totalAndaresPredio(self) -> int:
        return self._totalAndaresPredio
    
    @property
    def andarAtual(self) -> int:
        return self._andarAtual        

    @totalAndaresPredio.setter
    def totalAndaresPredio(self, totalAndaresPredio: int):
        self._totalAndaresPredio = totalAndaresPredio