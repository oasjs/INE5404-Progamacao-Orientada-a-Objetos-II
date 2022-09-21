class Televisao():
    def __init__(self, on:False, size: int, brand: str, channel: int, max_channel = 14, min_channel = 2) -> None:
        self.__on = on
        self.__size = size
        self.__brand = brand

        self.__channel = channel
        self.__max_channel = max_channel
        self.__min_channel = min_channel


    # Methods for size
    def get_size(self):
        return self.__size

    def set_size(self, size_value: float):
        if size_value >= 0:
            self.__size = size_value


    # Methods for brand
    def get_brand(self):
        return self.__brand

    def set_brand(self, brand_name: str):
        self.__brand = brand_name


    # Methods for channel
    def get_channel(self):
        return self.__channel

    def channel_up(self):
        self.__channel += 1
        if self.__channel > self.__max_channel:
            self.__channel = self.__min_channel

    def channel_down(self):
        self.__channel -= 1
        if self.__channel < self.__min_channel:
            self.__channel = self.__max_channel