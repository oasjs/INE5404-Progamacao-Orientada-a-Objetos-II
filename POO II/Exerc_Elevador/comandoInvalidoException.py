class ComandoInvalidoException(Exception):
    def __init__(self) -> None:
        super().__init__("Um ou mais parâmetros de inicialização do elevador são inválidos. Tenha certeza de que todos eles são inteiros não negativos. Tenha certeza também que os valores de andar atual e número de pessoas no elevador não são maiores que seus limites.")