class Cidade():
    def __init__(self, name:str, population:int) -> None:
        self._c_name = name
        self._c_population = population

    def get_city(self):
        return [self._c_name, self._c_population]


class Estado(Cidade):
    def __init__(self, name:str, alpha_code:str) -> None:
        self.__s_name = name
        self.__alpha_code = alpha_code
        self.__city_list = []


    def get_city_list(self):
        return " ".format(self.__city_list)

    
    def add_city(self, *cities:list):
        for city in cities:
            self.__city_list.append(city)






SC = Estado("Santa Catarina", "SC")
print(type(SC))