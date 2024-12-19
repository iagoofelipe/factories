# Requisitos Funcionais

- controle de itens em estoque, com suas respectivas características
- o sistema deve conter um menu de produtos
- o sistema deve permitir que o usuário escolha um produto e exiba os passsos necessários para a geração do item, a partir da quantidade necessária, recursos disponíveis em estoque e tempo de fabricação

## Item de Inventário
Objeto que deverá ser armazenado no inventário. Cada item deverá conter as seguintes características:

- recursos: conjunto de materiais necessários para gerar o item, relação entre [Item de Inventário](#item-de-inventário) e a quantidade necessária
- estoque: quantidade disponível em estoque
- [Fábrica](#fábrica): onde o item pode ser fabricado
- tempo de produção: tempo gasto para gerar o item, caso possua todos os recursos disponíveis.

## Fábrica
Local de fabricação dos [Itens de Inventário](#item-de-inventário). A fábrica pode conter recursos temporários de aceleração x durante um período n, ou seja, durante este período, o tempo gasto real será x vezes menor que o necessário.

## Objeto Final
Objeto que utilizará os recursos e poderá ir para a [Fila de Construção](#fila-de-construção).

## Fila de Construção
A fila de construção agrupa todos os recursos necessários e ordena-os de forma que seja levado o menor tempo necessário de acordo com o que há em estoque e o que é necessário ser fabricado.