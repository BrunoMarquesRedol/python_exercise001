from random import randint


def sorteia(n):
    '''Retorna uma lista com n valores aleatórios entre 1 e 10.'''
    return [randint(1, 10) for i in range(n)]

def par(x):
    '''Retorna True se x for par, False caso contrário.'''
    return x % 2 == 0

def soma_par(valores):
    '''Retorna a soma dos valores pares.'''
    return sum([v for v in valores if par(v)])


print('Sorteando 5 valores da lista: ', end='')
valores = sorteia(5)
for v in valores: print(f'{v} ', end='')
print('PRONTO!')
print(f'Somando os valores pares de {valores}, temos {soma_par(valores)}')
