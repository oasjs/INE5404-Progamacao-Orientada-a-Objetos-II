class ElevadorJahVazioException(Exception):
    def __init__(self) -> None:
        super().__init__("Elevador já está vazio!")