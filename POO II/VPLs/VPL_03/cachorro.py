from mamifero import Mamifero

class Cachorro(Mamifero):
    def __init__(self):
        super().__init__(volume_som=3, tamanho_passo=3)

    def produzirSom(self, volumeSom):
        return f'MAMIFERO: PRODUZ SOM: {volumeSom} SOM: '

    def latir(self):
        return self.produzirSom(volumeSom=3) + " AU"