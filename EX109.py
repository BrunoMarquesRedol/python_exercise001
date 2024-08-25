
from moedas import moeda, metade, aumentar, dobro



p = float(input('Digite o preço em R$ '))
print(f'A metade de {moeda(p, False)} é {moeda(metade(p), False)}')
print(f'O dobro de {moeda(p, True)} é {moeda(dobro(p), True)}')
print(f'Aumentando 10%, temos {moeda(aumentar(valor=p, p=10), True)}')