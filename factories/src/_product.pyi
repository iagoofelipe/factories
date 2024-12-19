from typing import overload
from ._factory import Factory

class FactoryProduct:
    @overload
    def __init__(self, name:str, time:int, factory:Factory) -> None: ...
    @overload
    def __init__(self, name:str, time:int, factory:Factory, resources:list) -> None: ...

    @property
    def time(self) -> int:
        """ duração para produção em minutos """
    
    @property
    def name(self) -> str:
        """ nome do produto """

    @property
    def factory(self) -> Factory:
        """ fabrica onde o produto é gerado """

    @property
    def resources(self) -> list[tuple[FactoryProduct, int]]:
        """ recursos necessários para a produção do item, relação entre o produto e quantidade necessária """

    def display(self) -> None:
        """ exibe os dados do produto no console """