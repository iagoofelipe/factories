class Factory:
    def __init__(self, name:str, capacity:int):
        """ Local de fabricação dos Itens de Inventário """

    @property
    def name(self) -> str: ...
    
    @property
    def capacity(self) -> int: ...