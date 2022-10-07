
# A classe Transporte deve possuir os atributos privados: nome, altura, comprimento, carga e velocidade
class Transporte():
    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, velocidade: float):
        self.__nome = nome
        self.__altura = altura
        self.__comprimento = comprimento
        self.__carga = carga
        self.__velocidade = velocidade

    @property
    def nome(self):
        return self.__nome

    @property
    def altura(self):
        return self.__altura

    @property
    def comprimento(self):
        return self.__comprimento

    @property
    def carga(self):
        return self.__carga

    @property
    def velocidade(self):
        return self.__velocidade

class TransporteAereo(Transporte):
    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, velocidade: float, autonomia: float, envergadura: float):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__autonomia = autonomia
        self.__envergadura = envergadura

    @property
    def autonomia(self):
        return self.__autonomia

    @property
    def envergadura(self):
        return self.__envergadura

class TransporteTerrestre(Transporte):
    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, velocidade: float, rodas: str, motor: str):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__rodas = rodas
        self.__motor = motor

    @property
    def rodas(self):
        return self.__rodas

    @property
    def motor(self):
        return self.__motor

class TransporteAquatico(Transporte):
    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, velocidade: float, boca: float, calado: float):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__boca = boca
        self.__calado = calado

    @property
    def boca(self):
        return self.__boca

    @property
    def calado(self):
        return self.__calado
