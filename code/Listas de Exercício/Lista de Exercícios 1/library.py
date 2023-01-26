class Book():
    def __init__(self, title:str, author:str, year:int, publisher:str, edition:int, volume:int) -> None:

        self._title = title
        self._author = author
        self._year = year
        self._publisher = publisher
        self._edition = edition
        self._volume = volume


    def get_info(self):

        book_info = {
            "Title": self._title,
            "Author": self._author,
            "Year": self._year,
            "Publisher": self._publisher,
            "Edition": self._edition,
            "Volume": self._volume
        }

        for info in book_info:
            print(f'{info}: {book_info[info]}')