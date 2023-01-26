'''Escreva uma função que conta a frequência de ocorrência de cada
palavra em um texto (arquivo txt) e armazena tal quantidade em um dicionário, onde a
chave é a vogal considerada.'''

def word_frequency(path:str):

    word_counter = {}

    with open(path, 'r', encoding='utf-8') as f:
        f = f.read()
        f = f.lower()
        f = f.split()
        f.sort()

        for word in f:
            word_counter.update({word: f.count(word)})
            
        return word_counter