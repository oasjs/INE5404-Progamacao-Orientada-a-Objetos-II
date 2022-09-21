from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        self._elevador = None

    '''
    Faz o elevador subir um andar. Se jah estiver no ultimo andar, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador 
    @throws ElevadorJahNoUltimoAndarException 
    '''
    
    def subir(self) -> str:
        return self._elevador.subir()
    
    '''
    Faz o elevador descer um andar. Se jah estiver no terreo, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorJahNoTerreoException
    '''
    
    def descer(self) -> str:
        return self._elevador.descer()

    '''
    Entra uma pessoa no Elevador. Se nao for possivel permitir a entrada da pessoa, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorCheioException
    '''
    
    def entraPessoa(self) -> str:
        return self._elevador.entraPessoa()
	
    '''
    Sai uma pessoa no Elevador. Se nao for possivel permitir a saida de uma pessoa, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorJahVazioException
    '''
    
    def saiPessoa(self) -> str:
        return self._elevador.saiPessoa()

    '''
    @return Elevador
    '''
    @property
    def elevador(self) -> Elevador:
        return self._elevador

    '''
    @param andarAtual andar atual do elevador
    @param totalAndaresPredio total de andares do predio
    @param capacidade capacidade maxima do elevador
    @param totalPessoas total de pessoas atual do elevador
    '''
    
    def inicializarElevador(self, andarAtual: int, totalAndaresPredio: int, capacidade: int, totalPessoas: int):

        if type(andarAtual) != int or type(totalAndaresPredio) != int or type(capacidade) != int or type(totalPessoas) != int:
            raise ComandoInvalidoException

        elif andarAtual < 0 or totalAndaresPredio < 0 or capacidade < 0 or totalPessoas < 0:
            raise ComandoInvalidoException 

        elif (andarAtual > totalAndaresPredio) or (totalPessoas > capacidade):
            raise ComandoInvalidoException

        else:
            self._elevador = Elevador(andarAtual, totalAndaresPredio, capacidade, totalPessoas)