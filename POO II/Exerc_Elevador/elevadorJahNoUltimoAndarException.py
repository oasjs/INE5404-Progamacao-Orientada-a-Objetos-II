class ElevadorJahNoUltimoAndarException(Exception):
    def __init__(self) -> None:
        super().__init__("Elevador já está no último andar!")

