import pickle
from empresa import Empresa

class EmpresaDAO:
    def __init__(self, datasource='empresa.pkl'):
        self.__datasource = datasource
        self.__object_cache = {}

    def __dump(self):
        with open(self.__datasource, 'wb') as file:
            pickle.dump(self.__object_cache, file)

    def __load(self):
        with open(self.__datasource, 'rb') as file:
            self.__object_cache = pickle.load(file)

    def get(self, cnpj: int) -> Empresa:
        for empresa in self.__object_cache.values():
            if empresa.cnpj == cnpj:
                return empresa

    def add(self, empresa: Empresa):
        self.__object_cache[empresa.cnpj] = empresa

    def remove(self, empresa: Empresa):
        self.__object_cache.pop(empresa.cnpj)

    def get_all(self) -> list:
        return self.__object_cache.values()
