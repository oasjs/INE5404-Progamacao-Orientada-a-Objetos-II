from mamifero import Mamifero

class Gato(Mamifero):
    def __init__(self):
        super().__init__(volume_som=2, tamanho_passo=2)

    def produzirSom(self, volumeSom):
        return f'MAMIFERO: PRODUZ SOM: {volumeSom} SOM: '

    def miar(self):
        return self.produzirSom(volumeSom=2) + " MIAU"