
from random import shuffle

v1 = 'Já fez algo de que se arrependa?,se sim o que?'
v2 = 'Ja tirou o BV?'
v3 = 'Você tem um dia inesquecivel?, se sim como foi?'
v4 = 'Você ja desistiu de algo muito importante?, se sim o que foi?'
v5 = 'Já sofreu ou praticou bullying na escola?'
v6 = 'Tem algum grande desejo?qual?'
v7 = 'Ja entrou em uma briga?como foi?'
v8 = 'Você quer ter filhos?, se sim quantos?'

d1 = 'Imite um macaco'
d2 = 'Deixe a pessoa do seu lado direito te daar um tapa'
d3 = 'Teve sorte, pule a sua vez'
d4 = 'Fale uma raça de cachorro que começa com y, se não conseguir imite um '
d5 = 'Não fale nada pelos proximos 5 minutos'
d6 = 'Fale para uma pessoa que não está na brincadeira que a ama( não vale parente)'
d7 = 'Você so poderá escolher desafio nas proximas 5 rodadas'
d8 = 'Agora você tem poder, mande um dos jogadores fazer o que você quiser'

lista_v = [v1, v2, v3, v4, v5, v6, v7, v8]
lista_d = [d1, d2, d3, d4, d5, d6, d7, d8]

print ('Caso queira verdade escreva v,se quiser desafio escreva d.')

while True:
  shuffle(lista_v)
  shuffle(lista_d)

  d_v = input('Você escolhe verdade ou desafio ?')

  if d_v == 'v' :
    print('{}'.format(lista_v[0]))
  elif d_v == 'd':
    print('{}'.format(lista_d[0]))