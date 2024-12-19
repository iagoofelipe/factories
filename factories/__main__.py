from .src._app import Application

if __name__ == '__main__':
    app = Application()
    product = app.getProductByName('hambúrguer')
    
    if product is None:
        print('produto não encontrado!')
    else:
        product.display()

    product = app.getProductById(15)

    if product is None:
        print('produto não encontrado!')
    else:
        product.display()