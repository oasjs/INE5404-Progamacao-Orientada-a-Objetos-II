import pickle
from empresa import Empresa
import os

class EmpresaDAO:
    def __init__(self, datasource='empresa.pkl') -> None:
        self.__datasource = datasource
        self.__object_cache = {}
        if os.path.exists(datasource) and os.path.getsize(datasource) > 0:
            self.__load()

    def __dump(self) -> None:
        with open(self.__datasource, 'wb') as file:
            pickle.dump(self.__object_cache, file)

    def __load(self) -> None:
        with open(self.__datasource, 'rb') as file:
            self.__object_cache = pickle.load(file)

    def get(self, cnpj: int) -> Empresa:
        for empresa in self.__object_cache.values():
            if empresa.cnpj == cnpj:
                return empresa

    def add(self, empresa: Empresa) -> None:
        self.__object_cache.update({empresa.cnpj: empresa})
        self.__dump()

    def remove(self, empresa: Empresa) -> None:
        self.__object_cache.pop(empresa.cnpj)
        self.__dump()

    def get_all(self) -> list:
        return self.__object_cache.values()
