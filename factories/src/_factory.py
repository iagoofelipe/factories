class Factory:
    """ Local de fabricação dos Itens de Inventário """
    def __init__(self, name:str, capacity:int):
        self.__name = name
        self.__capacity = capacity

    @property
    def name(self): return self.__name
    
    @property
    def capacity(self): return self.__capacity