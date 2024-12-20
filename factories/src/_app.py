from sqlite3 import connect
from queue import Queue

from ._factory import Factory
from ._product import FactoryProduct

class Application:
    def __init__(self):
        self.__conn = connect('database.sqlite3')
        self.__cursor = self.__conn.cursor()

        self.generate()

    @property
    def products(self) -> list[FactoryProduct]:
        return list(self.__products_id.values())
    
    def getProductByName(self, name:str) -> FactoryProduct | None:
        return self.__products_name.get(name)
    
    def getProductById(self, productId:int) -> FactoryProduct | None:
        return self.__products_id.get(productId)

    def generate(self):
        """ gera as estruturas a partir da base de dados """
        self.__generateFactory()
        self.__generateProduct()
        self.__generateInventory()

    def updateInventory(self, product:FactoryProduct, quantity:int, add=False):
        product_id = product.id

        if product_id in self.__inventory:
            if add:
                quantity += self.__inventory[product_id]
            cmd = 'UPDATE inventory_product SET quantity=? WHERE product_id=?'
        else:
            cmd = 'INSERT INTO inventory_product (quantity, product_id) VALUES (?, ?)'

        self.__cursor.execute(cmd, (quantity, product_id))
        self.__conn.commit()
        self.__generateInventory()
    
    def constructNewProduct(self, product:FactoryProduct, use_inventory=True, update_inventory=False) -> tuple[tuple[FactoryProduct, int]]:
        required_resources = {}
        inventory = {}
        queue:Queue[tuple[FactoryProduct, int]] = Queue()

        # adicionando à fila de verificação de recursos
        for rsc in product.resources:
            queue.put(rsc)
        
        while not queue.empty():
            # verificando recursos necessários
            product, quantity = queue.get()
            product_id = product.id
            
            # caso utilize do inventário
            if use_inventory: # TODO: juntar recursos necessários na consulta ao inventário

                if product_id not in inventory:
                    inventory[product_id] = self.getInventory(product)

                # verificando quantidade disponível em estoque
                if quantity > inventory[product_id]: # caso não tenha a quantidade necessária
                    if product_id not in required_resources:
                        required_resources[product_id] = 0
                    
                    required_resources[product_id] += quantity - inventory[product_id]
                    inventory[product_id] = 0
                    
                    # adicionando à fila de verificação de recursos
                    for p, qtd in product.resources:
                        queue.put((p, qtd*quantity))

                else:
                    inventory[product_id] -= quantity
            
            else:
                if product_id not in required_resources:
                    required_resources[product_id] = 0
                
                required_resources[product_id] += quantity

                # adicionando à fila de verificação de recursos
                for p, qtd in product.resources:
                    queue.put((p, qtd*quantity))

        return tuple([(self.__products_id[k], v) for k, v in required_resources.items()])

    
    def getInventory(self, product:FactoryProduct) -> int:
        """ retorna a quantidade disponível em estoque para um produto """
        return self.__inventory.get(product.id, 0)
    
    def checkInventory(self, product:FactoryProduct, quantity=1) -> bool:
        """ verifica se há a quantidade desejada em estoque """
        return quantity <= self.getInventory(product)

    def removeFromInventory(self, product:FactoryProduct, quantity=1) -> bool:
        if not self.checkInventory(product, quantity):
            return False
        
        quantity = self.getInventory(product) - quantity
        self.updateInventory(product, quantity)
        return True

    def __generateFactory(self):
        self.__factories_id = {}
        self.__factories_name = {}

        self.__cursor.execute('SELECT * FROM factory')
        for _id, name, capacity in self.__cursor.fetchall():
            factory = Factory(name, capacity)

            # armazenando objeto gerado
            self.__factories_id[_id] = factory
            self.__factories_name[name] = factory

    def __generateProduct(self):
        self.__products_id = {}
        self.__products_name = {}

        self.__cursor.execute('SELECT * FROM product')
        for _id, name, time, factory_id, time_base in self.__cursor.fetchall():
            time *= time_base
            factory = self.__factories_id[factory_id]
            product = FactoryProduct(_id, name, time, factory)
            
            # armazenando objeto gerado
            self.__products_id[_id] = product
            self.__products_name[name] = product

        # gerando resources de cada product
        self.__cursor.execute('SELECT * FROM product_resource')
        for _id, product_id, rsc_id, quantity in self.__cursor.fetchall():
            self.__products_id[product_id].resources.append((self.__products_id[rsc_id], quantity))

    def __generateInventory(self):
        self.__inventory = {}

        self.__cursor.execute('SELECT * FROM inventory_product')
        for _id, product_id, quantity in self.__cursor.fetchall():
            self.__inventory[product_id] = quantity