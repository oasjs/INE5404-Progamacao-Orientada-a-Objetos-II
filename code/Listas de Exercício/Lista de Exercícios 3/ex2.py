'''Escreva uma função que apaga do dicionário anterior, todas as palavras
que sejam ​‘stopwords​’. Ver https://gist.github.com/alopes/5358189'''

def remove_stopwords(word_dict:dict):
    with open("./stopwords.txt", 'r', encoding='utf-8') as f:
        f = f.read()
        for word in f.split():
            if word in word_dict.keys():
                del word_dict[word]

    return word_dict