
from random import randint
from time import sleep
print('Seu carro passou no radar ...')
sleep(2)
vel = randint(10,180)
if vel > 80:
    print('Você estava a {}Km/h e foi multado, o valor da multa é R${:.2f}'.format(vel, (vel-80)*7))
else:
    print('Sua velocidade é {}Km/h, continue respeitando os limites'.format(vel))