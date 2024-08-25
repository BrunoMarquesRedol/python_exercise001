
cont1 = contvl = contmil = 0
contmaisbarato = contmaiscaro = ''

print('*'*30,'VAMOS AS COMPRAS','*'*30)

while True:
  produto = str(input('Qual o nome do produto? '))
  valor = float(input('Qual o valor desse produto? R$'))

  print(':'*78)
  if valor >= 1000:
    contmil += 1
  contvl += valor
  cont1 += 1
  if cont1 == 1:
    maisbarato = valor
  if valor < maisbarato:
    contmaisbarato = produto
    maisbarato = valor
  if cont1 == 1:
    maiscaro = valor
  if valor > maiscaro:
    contmaiscaro = produto
    maiscaro = valor

  pergunta = str(input('Quer continuar [S/N]? '))
  if pergunta in 'Nn':
    break
print(f'Você comprou {cont1} itens e gastou R${contvl:.2f}')
print(f'Existem {contmil} produtos acima de R$1000,00 reais!')
print(f'O produto mais barato é {contmaisbarato} e custa R${maisbarato}')
print(f'O produto mais caro é {contmaiscaro} e custa R${maiscaro}')
print('='*30, 'PROGRAMA ENCERRADO','='*30)