from sqlite3 import connect

from ._factory import Factory
from ._product import FactoryProduct

class Application:
    def __init__(self):
        self.__conn = connect('database.sqlite3')
        self.__cursor = self.__conn.cursor()

        self.generate()

    def generate(self):
        """ gera as estruturas a partir da base de dados """
        self.__products_id = {}
        self.__products_name = {}
        self.__factories_id = {}
        self.__factories_name = {}

        # gerando factories
        self.__cursor.execute('SELECT * FROM factory')
        for _id, name, capacity in self.__cursor.fetchall():
            factory = Factory(name, capacity)

            # armazenando objeto gerado
            self.__factories_id[_id] = factory
            self.__factories_name[name] = factory

        # gerando products
        self.__cursor.execute('SELECT * FROM product')
        for _id, name, time, factory_id, time_base in self.__cursor.fetchall():
            time *= time_base
            factory = self.__factories_id[factory_id]
            product = FactoryProduct(name, time, factory)
            
            # armazenando objeto gerado
            self.__products_id[_id] = product
            self.__products_name[name] = product

        # gerando resources de cada product
        self.__cursor.execute('SELECT * FROM product_resource')
        for _id, product_id, rsc_id, quantity in self.__cursor.fetchall():
            self.__products_id[product_id].resources.append((self.__products_id[rsc_id], quantity))

    
    @property
    def products(self) -> list[FactoryProduct]:
        return list(self.__products_id.values())
    
    def getProductByName(self, name:str) -> FactoryProduct | None:
        return self.__products_name.get(name)
    
    def getProductById(self, productId:int) -> FactoryProduct | None:
        return self.__products_id.get(productId)