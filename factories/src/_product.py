class FactoryProduct:
    def __init__(self, name, time, factory, resources=None):
        self.__name = name
        self.__time = time
        self.__factory = factory
        self.__resources = [] if resources is None else resources

    def __str__(self):
        return f'<FactoryProduct={self.__name}>'
    
    def __repr__(self):
        return self.__str__()
    
    @property
    def time(self):
        return self.__time
    
    @property
    def name(self):
        return self.__name

    @property
    def factory(self):
        return self.__factory

    @property
    def resources(self):
        return self.__resources

    @resources.setter
    def resources(self, v):
        self.__resources = v

    def display(self):
        print(self, *[f'\tRequisito: {obj}, qtd={qtd}' for (obj, qtd) in self.__resources], sep='\n')