
soma = 0
for numero in range(0, 6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero
else:
    print('Não foram digitados números pares)')
print('A soma dos pares foi de :'soma).format(soma)