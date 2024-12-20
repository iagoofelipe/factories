from .src._app import Application

if __name__ == '__main__':
    app = Application()
    
    # cadastrando 5 rações e 3 metais
    # app.updateInventory(app.getProductByName('ração'), 5)
    # app.updateInventory(app.getProductByName('metal'), 3)
    
    # product = app.getProductByName('hambúrguer')

    # print(f'recursos necessários sem estoque:')
    # for p, qtd in app.constructNewProduct(product, False):
    #     print(f'\t{p}: {qtd} unidade(s)')

    # print(f'recursos necessários com estoque:')
    # for p, qtd in app.constructNewProduct(product):
    #     print(f'\t{p}: {qtd} unidade(s)')


    print(app.constructNewProduct(app.getProductByName('cheesecake de cereja'), False))
    print()
    print(app.constructNewProduct(app.getProductByName('sanduíche de sorvete'), False))