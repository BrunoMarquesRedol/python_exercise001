
def resumo(preco, aumento=10, desconto=5):
    print('-' * 35)
    print(f'RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{desconto}% de desconto: \t{aumentar(preco, desconto, True)}')