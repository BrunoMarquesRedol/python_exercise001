Módulo moeda.py


def aumentar(valor, percentual):
    """
    → Função para aumentar o valor de acordo com o percentual.
    :param valor: que será aumentado
    :param percentual: que será aplicado ao valor
    :return: o valor com o reajuste percentual
    """

    return valor + (valor * percentual / 100)


def diminuir(valor, percentual):
    """
    → Função para diminuir o valor de acordo com o percentual.
    :param valor: que será reduzido
    :param percentual: que será aplicado ao valor
    :return: o valor com o reajuste percentual
    """

    return valor - (valor * percentual / 100)


def dobro(valor):
    """
    → Função para dobrar um valor
    :param valor: que será dobrado
    :return: valor dobrado
    """

    return valor * 2


def metade(valor):
    """
    → Função para dividir um valor ao meio
    :param valor: que será divido
    :return: do valor dividio ao meio
    """

    return valor / 2

ex107.py

"""
 Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
 Faça também um programa que importe esse módulo e use algumas dessas funções.

"""


from Módulos import moeda


preco = float(input('Digite o preço: '))
print(f'A metade de R${preco} é R${moeda.metade(preco)}')
print(f'O dobro de R${preco} é R${moeda.dobro(preco)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10)}')
