'''Escreva uma função que conta a frequência de ocorrência de cada
palavra em um texto (arquivo txt) e armazena tal quantidade em um dicionário, onde a
chave é a vogal considerada.'''

def vowel_frequency(path:str):

    vowels = ['A','E','I','O','U']
    counter_dict = {}
    for vowel in vowels:
        counter_dict.setdefault(vowel, 0) # setdefault method inserts key with specified value, if the key does not exist.

    with open(path, 'r') as f:
        f = f.read()
        f = f.upper()

        for vowel in counter_dict:
            counter_dict.update({vowel:f.count(vowel)})