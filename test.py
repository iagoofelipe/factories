from factories.src._app import Application
from queue import Queue
from sqlite3 import connect

app = Application()
produto = app.getProductByName('hambúrguer')
cursor = connect('database.sqlite3').cursor()

# queue = Queue()

# # consulta os recursos do produto a ser gerado
# for item in filter(lambda x: app.checkInventory(*x), produto.resources):
    # queue.put(item)

queue = tuple(filter(lambda x: not app.checkInventory(*x), produto.resources))
results = []

for p, qtd in queue:
    cursor.execute('SELECT * FROM product_resource WHERE product_id=?', (p.id, ))
    results.extend(cursor.fetchall())

print(queue)
print(results)