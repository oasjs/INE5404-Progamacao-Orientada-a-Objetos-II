class ElevadorJahNoTerreoException(Exception):
    def __init__(self) -> None:
        super().__init__("Elevador já está no térreo!")
    
