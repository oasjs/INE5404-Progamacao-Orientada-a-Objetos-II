from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__listaChamados = []
        self.__listaTiposChamados = []

    def totalChamadosPorTipo(self, tipo: TipoChamado) -> int:
        count = 0 
        for c in self.__listaChamados:
            if c.tipo == tipo:
                count += 1

        return count

    def incluiChamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: str, tipo: TipoChamado) -> Chamado:
        chamado = Chamado(data, cliente, tecnico, titulo, descricao, prioridade, tipo)
        check = True
        for c in self.__listaChamados:
            if c.data == data and c.cliente == cliente and c.tecnico == tecnico and c.tipo == tipo:
                check = False
                break

        if check:    
            self.__listaChamados.append(chamado)
            return chamado

    def incluiTipoChamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
        tipoChamado = TipoChamado(codigo, nome, descricao)
        check = True
        for t in self.__listaTiposChamados:
            if id(t) == id(tipoChamado):
                check = False
                break

        if check:
            self.__listaTiposChamados.append(tipoChamado)
            return tipoChamado

    @property
    def tipoChamados(self):
        return self.__listaTiposChamados

    @property
    def chamados(self):
        return self.__listaChamados
