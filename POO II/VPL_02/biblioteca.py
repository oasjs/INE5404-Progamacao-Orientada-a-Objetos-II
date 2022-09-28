from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluirLivro(self, livro: Livro):
        #Nao esqueca de garantir que o objeto recebido pertence a classe Livro...
        if isinstance(livro, Livro):
            if livro not in self.__livros:
                self.__livros.append(livro)
            else:
                print("Livro já cadastrado")
        # else:
        #     raise TypeError("O objeto não é do tipo Livro")

    def excluirLivro(self, livro: Livro):
        if isinstance(livro, Livro):
            if livro in self.__livros:
                self.__livros.remove(livro)
            else:
                print("Livro não cadastrado")
        # else:
        #     raise TypeError("O objeto não é do tipo Livro")

    @property
    def livros(self):
        return self.__livros
