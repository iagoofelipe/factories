class Factory:
    def __init__(self, name, capacity):
        self.__name = name
        self.__capacity = capacity

    @property
    def name(self): return self.__name
    
    @property
    def capacity(self): return self.__capacity