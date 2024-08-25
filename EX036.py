
from time import sleep
print('Olá, seja muito bem vindo a nossa simulação de financiamento :)')
inicio = input('A perte \033[34mEnter\033[m para iniciarmos! ')
sleep(1)
imovel = float(input('Digite o valor do bem que deseja adquirir: '))
salario = float(input('Qual o seu salário atualmente? '))
prazo = int(input('Em quantas vezes deseja parcelar? '))
print('Aguarde...')
sleep(2)
juros = 0.10 / 100
j_total = prazo * 0.10
sd = (imovel * (100 + j_total) / 100)
parcela = sd / prazo
condicao = (salario * 30) / 100

if parcela > condicao:
    print('\033[1;33m-=-\033[m'*20)
    print('Crédito R$ {:.2f}'.format(imovel))
    print('Prazo {} Meses'.format(prazo))
    print('\033[31mParcela R$ {:.2f}\033[m'.format(parcela))
    print('Lamento, mas seu financiamento não foi aprovado,')
    print('o valor de parcela excerdeu 30% da sua renda.')
    print('Gostaria de fazer outras simulação? ')
    print('\033[1;33m-=-\033[m' * 20)

else:
    print('\033[1;33m-=-\033[m' * 20)
    print('Crédito R$ {:.2f}'.format(imovel))
    print('Prazo de {} Meses'.format(prazo))
    print('Parcela de R$ {:.2f}'.format(parcela))
    print('Parabéns, seu financiamneto foi aprovado!!')
    print('Vamos já iniciar o seu sonho da casa própria :)')
    print('\033[1;33m-=-\033[m' * 20)