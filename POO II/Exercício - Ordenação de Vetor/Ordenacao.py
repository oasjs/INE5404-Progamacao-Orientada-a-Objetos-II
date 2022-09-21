"""
   Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""

class Ordenacao():

    def __init__(self, array_para_ordenar:list):
        """Recebe o array com o conteudo a ser ordenado"""
        
        self.array = array_para_ordenar
        self.check = 0


    def ordena(self):
        """Realiza a ordenacao do conteudo do array recebido no construtor"""
        
        for i in range(len(self.array)):
            for j in range(len(self.array)):
                if self.array[i] < self.array[j]:
                    temp = self.array[i]
                    self.array[i] = self.array[j]
                    self.array[j] = temp

        return self.array


    def toString(self):
        """Converte o conteudo do array em String formatado
           Exemplo: 
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
        """

        for i in range(len(self.array)):
            self.array[i] = str(self.array[i])

        formated_string = ",".join(self.array)
        
        return formated_string