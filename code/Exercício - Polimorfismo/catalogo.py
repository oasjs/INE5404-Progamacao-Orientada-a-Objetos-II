from transporte import *

class Catalogo:
    def __init__(self) -> None:
        self.__veiculos = []

    def insercao(self, transporte: Transporte):
        if isinstance(transporte, Transporte):
            self.__veiculos.append(transporte)
        else:
            print('Não é um veículo!')

    def apresentacao(self):
        print('Veículos cadastrados:')
        for veiculo in self.__veiculos:
            print(veiculo.nome)