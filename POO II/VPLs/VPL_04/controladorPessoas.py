from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    def incluiCliente(self, codigo: int, nome: str) -> Cliente:
        cliente = Cliente(nome, codigo)
        check = True
        for c in self.clientes:
            if c.codigo == cliente.codigo:
                check = False

        if check:
            self.__clientes.append(cliente)
            return cliente

    def incluiTecnico(self, codigo: int, nome: str) -> Tecnico:
        tecnico = Tecnico(nome, codigo)
        check = True
        for t in self.tecnicos:
            if t.codigo == tecnico.codigo:
                check = False

        if check:
            self.__tecnicos.append(tecnico)
            return tecnico
            