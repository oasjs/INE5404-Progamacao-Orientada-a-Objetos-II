from AbstractMesa import *


class Mesa(AbstractMesa):

    #Construtor fornecido, nao deve ser alterado
    def __init__(self, jogador1: Jogador, jogador2: Jogador,
                 cartaJogador1: Carta, carta_jogador2: Carta):
        self.__jogador1 = jogador1
        self.__jogador2 = jogador2
        self.__cartaJogador1 = cartaJogador1
        self.__carta_jogador2 = carta_jogador2

    @property
    def jogador1(self) -> Jogador:
        return self.__jogador1

    @property
    def jogador2(self) -> Jogador:
        return self.__jogador2

    @property
    def carta_jogador1(self) -> Carta:
        return self.__cartaJogador1

    @property
    def carta_jogador2(self) -> Carta:
        return self.__carta_jogador2
