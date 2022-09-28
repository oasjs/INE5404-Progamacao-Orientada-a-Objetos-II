from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora    
        self.__autores = []
        self.__capitulos = []
        self.incluirAutor(autor)
        self.incluirCapitulo(numeroCapitulo, tituloCapitulo)

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo

    @property
    def ano(self):
        return self.__ano

    @property
    def editora(self):
        return self.__editora

    @property
    def autores(self):
        return self.__autores


    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @editora.setter
    def editora(self, editora: Editora):
        self.__editora = editora


    def incluirAutor(self, autor: Autor):
        # Nao esqueca de garantir que o objeto recebido pertence a classe Autor...
        # Nao permitir insercao de Autores duplicados!
        if isinstance(autor, Autor):    
            if autor not in self.__autores:
                self.__autores.append(autor)
            else:
                print("Autor já cadastrado!")
        else:
            print("O objeto não pertence a classe Autor!")

    def excluirAutor(self, autor: Autor):
        if autor in self.__autores:
            self.__autores.remove(autor)
        else:
            print("Autor não cadastrado!")

    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        # Nao permitir insercao de Capitulos duplicados!
        if self.findCapituloByTitulo(tituloCapitulo) == None:
            self.__capitulos.append(Capitulo(numeroCapitulo, tituloCapitulo))
        else:
            print("Capítulo já existe!")

    def excluirCapitulo(self, tituloCapitulo: str):
        if self.findCapituloByTitulo(tituloCapitulo) != None:
            self.__capitulos.remove(self.findCapituloByTitulo(tituloCapitulo))
        else:
            print("Capítulo não existe!")

    def findCapituloByTitulo(self, tituloCapitulo: str):
        for capitulo in self.__capitulos:
            if capitulo.titulo == tituloCapitulo:
                return capitulo
            else:
                return None